from celery import shared_task

from core import settings

from django.core.mail import send_mail


@shared_task()
def send_massage(subject, message, recipient_list=settings.EMAIL_HOST_USER,
                 from_email=settings.EMAIL_HOST_USER):

    send_mail(subject=subject,
              message=message,
              from_email=from_email,
              recipient_list=[recipient_list])
