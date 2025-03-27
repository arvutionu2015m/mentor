from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import UserProfile, QuestionLog, ImageUpload
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Arvutionu Mentor – Õpetaja Admin")
admin.site.site_title = _("Mentor Admin")
admin.site.index_title = _("Tere tulemast Arvutionu Mentori haldussüsteemi")
admin.site.site_url = "/"


# ✅ Inline: UserProfile User-i sees
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0

# ✅ Inline: QuestionLog User-i sees
class QuestionLogInline(admin.TabularInline):
    model = QuestionLog
    extra = 0
    fields = ('question', 'answer', 'timestamp')
    readonly_fields = ('question', 'answer', 'timestamp')
    can_delete = False

# ✅ Laienda User adminit ja lisa mõlemad inline’id
class CustomUserAdmin(DefaultUserAdmin):
    inlines = [UserProfileInline, QuestionLogInline]    

# ✅ Jäta UserProfile nähtavaks, kui soovid eraldi vaates
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'is_approved')
    list_filter = ('status', 'is_approved')

@admin.register(QuestionLog)
class QuestionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_question', 'has_comment', 'timestamp')
    list_filter = ('timestamp', 'user')
    search_fields = ('user__username', 'question', 'answer', 'teacher_comment')
    fields = ('user', 'question', 'answer', 'teacher_comment', 'timestamp')
    readonly_fields = ('user', 'question', 'answer', 'timestamp')

    def short_question(self, obj):
        return obj.question[:50] + "..." if len(obj.question) > 50 else obj.question
    short_question.short_description = "Küsimus"

    def has_comment(self, obj):
        return bool(obj.teacher_comment)
    has_comment.boolean = True
    has_comment.short_description = "Kommentaar?"

# Juba olemas, aga lisame kindluse mõttes ka
@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at')
