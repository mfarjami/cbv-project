from celery import shared_task
from time import sleep
from CBV_todo.celery import app


@shared_task
def sendemail():
    sleep(3)
    return sendemail


@shared_task
def task_delete():
    sleep(5)
    app.control.purge()
    print("Deleted Task")