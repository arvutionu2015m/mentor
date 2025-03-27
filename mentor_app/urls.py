# mentor_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('teacher/add-student/', views.add_student, name='add_student'),
    path('my-questions/', views.my_questions_view, name='my_questions'),
    path('teacher/questions/', views.question_log_view, name='teacher_question_log'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/add-student/', views.add_student, name='add_student'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='account_login'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

]