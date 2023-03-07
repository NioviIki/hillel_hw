from django.shortcuts import render
from django.core.mail import send_mail
from celery import shared_task
from core.celery import app

import time
from .forms import TForm
from core import settings
# delay

def tes(request):
    forms = TForm
    if request.method == "POST":
        form = TForm(request.POST)
        if form.is_valid():
            form.send_massages()
            return render(request, 'send_email/tes.html', {'forms': TForm()})
        else:
            print(1)
    return render(request, 'send_email/tes.html', {'forms': forms})


