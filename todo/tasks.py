from celery import shared_task
from .models import Task


@shared_task
def task_delete():
    Task.objects.filter(done=True).delete()
    print("Deleted Task")