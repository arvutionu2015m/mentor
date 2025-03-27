from django.db import models
from django.contrib.auth.models import User

class QuestionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    teacher_comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} – {self.question[:50]}"


class UserProfile(models.Model):
    STATUS_CHOICES = [
        ('student', 'Õpilane'),
        ('teacher', 'Õpetaja'),
        ('parent', 'Vanem'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} – {self.get_status_display()}"


class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"

