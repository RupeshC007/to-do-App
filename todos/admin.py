from django.contrib import admin
from .models import Tasks
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('task',)

admin.site.register(Tasks, TaskAdmin)