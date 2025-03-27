from django.apps import AppConfig

class MentorAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mentor_app'

    def ready(self):
        import mentor_app.signals  # ← see on väga oluline!
