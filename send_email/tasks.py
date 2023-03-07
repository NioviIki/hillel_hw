from celery import shared_task
from django.core.mail import send_mail
from celery import shared_task

from core.celery import app
from core import settings
import time
@shared_task()
def send_massage(subject, message,  recipient_list=settings.EMAIL_HOST_USER, from_email=settings.EMAIL_HOST_USER):

    # time.sleep(tim)
    send_mail(subject=subject,
              message=message,
              from_email=from_email,
              recipient_list=[recipient_list])
