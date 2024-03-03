from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_to(theme, text, send_from, send_to):
    send_mail(theme, text, send_from, send_to)
