from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User

from .models import UserProfile, QuestionLog
from .forms import AddStudentForm  # Import the form
from .decorators import status_required
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

import openai

@login_required
def my_questions_view(request):
    logs = QuestionLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'my_questions.html', {'logs': logs})

@login_required
@status_required('teacher')
def add_student(request):
    form = AddStudentForm()  # ← defineerime alati alguses

    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            # Parool võib olla antud või genereeritakse juhuslikult
            password = form.cleaned_data['password'] or get_random_string(10)

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                password=password
            )
            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.status = 'student'
            profile.is_approved = True
            profile.save()

            # Saada e-kiri õpilasele
            send_mail(
                subject="Sinu konto on loodud Mentor-õppeportaalis",
                message=(
                    f"Tere {user.first_name or user.username},\n\n"
                    f"Sinu konto on loodud.\n"
                    f"Kasutajanimi: {user.username}\n"
                    f"Parool: {password}\n\n"
                    f"Logi sisse: http://127.0.0.1:8000/login/\n\n"
                    f"Tervitades,\nMentor Meeskond"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email]
            )

            messages.success(request, f"Õpilane {user.username} lisatud ja e-kiri saadetud!")
            return redirect('add_student')

    return render(request, 'add_student.html', {'form': form})

# ✅ Registreerimine (staatus valitakse)
def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        status = request.POST.get("status")

        if username and password and email and status:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name)
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.status = status
            profile.is_approved = False
            profile.save()
            login(request, user)
            messages.success(request, "Konto loodud. Staatus ootab kinnitamist.")
            return redirect('home')
        else:
            messages.error(request, "Kõik väljad on kohustuslikud.")
    return render(request, 'signup.html')


# ✅ Sisselogimine
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Sisselogimine õnnestus.")
            return redirect('home')
        else:
            messages.error(request, "Vale kasutajanimi või parool.")
    return render(request, 'login.html')


# ✅ Väljalogimine
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


# ✅ Avaleht: kasutaja küsib, ChatGPT vastab, salvestab logi
@login_required
def home(request):
    response = None
    if request.method == "POST":
        question = request.POST.get("question")
        if question:
            openai.api_key = settings.OPENAI_API_KEY
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Sa oled abistav mentor, kes selgitab õppematerjali ja esitab kontrollküsimusi."},
                        {"role": "user", "content": question}
                    ]
                )
                response = completion.choices[0].message['content']

                # salvesta küsimuste logi
                QuestionLog.objects.create(
                    user=request.user,
                    question=question,
                    answer=response
                )

            except Exception as e:
                response = "Viga ChatGPT vastuses: " + str(e)

    return render(request, 'home.html', {'response': response})


# ✅ Õpetaja juhtpaneel – õpilaste haldus ja lisamine
@login_required
@status_required('teacher')
def teacher_dashboard(request):
    students = UserProfile.objects.filter(status='student').select_related('user')
    student_count = students.count()  # ✅ lisame õpilaste arvu
    unapproved_users = UserProfile.objects.filter(is_approved=False).count()

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            temp_user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                password=password
            )
            profile, created = UserProfile.objects.get_or_create(user=temp_user)
            profile.status = 'student'
            profile.is_approved = True
            profile.save()

            # Saada e-kiri
            send_mail(
                subject="Sinu konto on loodud Mentor-õppeportaalis",
                message=(
                    f"Tere {first_name or username},\n\n"
                    f"Sinu kasutajakonto on loodud.\n"
                    f"Kasutajanimi: {username}\n"
                    f"Parool: {password}\n\n"
                    f"Logi sisse: http://127.0.0.1:8000/login/\n\n"
                    f"Tervitades,\nMentor Meeskond"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )

            messages.success(request, f"Õpilane {username} lisatud ja e-kiri saadetud!")
            return redirect('teacher_dashboard')
        else:
            messages.error(request, "Kõik väljad on kohustuslikud!")

    return render(request, 'teacher_dashboard.html', {
        'students': students,
        'student_count': student_count,
        'unapproved_users': unapproved_users
    })


# ✅ Küsimuste logi õpetajale
@login_required
@status_required('teacher')
def question_log_view(request):
    logs = QuestionLog.objects.select_related('user').order_by('-timestamp')

    if request.method == 'POST':
        log_id = request.POST.get('log_id')
        comment = request.POST.get('teacher_comment')
        try:
            log_entry = QuestionLog.objects.get(id=log_id)
            log_entry.teacher_comment = comment
            log_entry.save()
            messages.success(request, f'Kommentaar salvestatud küsimusele: {log_entry.question[:50]}...')
        except QuestionLog.DoesNotExist:
            messages.error(request, 'Küsimust ei leitud.')

        return redirect('teacher_question_log')

    return render(request, 'teacher_question_log.html', {'logs': logs})