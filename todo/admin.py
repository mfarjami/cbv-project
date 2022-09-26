from django.contrib import admin
from .models import Task
# Register your models here.

class AdminTask(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(Task, AdminTask)