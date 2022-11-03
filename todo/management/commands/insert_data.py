from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from todo.models import Task
import random

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(username=self.fake.color_name(), password="Aa123456*")
        user.first_name = self.fake.first_name
        user.email = self.fake.free_email()
        user.last_name = self.fake.last_name
        user.save()

        for _ in range(10):
            Task.objects.create(
                owner= user,
                title = self.fake.paragraph(nb_sentences=1),
                done = random.choice([True, False]),

            )
