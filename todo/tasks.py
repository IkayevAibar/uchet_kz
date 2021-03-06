import string

from .models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        email = '{}@example.com'.format(get_random_string(10, string.ascii_letters))
        password = get_random_string(50)
        User.objects.create_user(email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task
def send_message(user):
    pass