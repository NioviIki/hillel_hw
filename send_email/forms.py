from django import forms
from .tasks import send_massage
from django.contrib.admin import widgets
from datetime import datetime
from django.utils import timezone
from datetime import datetime, timedelta
import datetime


class TForm(forms.Form):
    subject = forms.CharField(max_length=20, label='Subject')
    message = forms.CharField(max_length=200, label='Message', widget=forms.Textarea)
    email = forms.EmailField(label='Email')
    time1 = forms.DateTimeField(label='Time', input_formats=['%d-%m-%Y %H:%M'])

    def send_massages(self):

        x = self.cleaned_data['time1'].day
        c = datetime.datetime.now()
        print(x - c)
        # print(datetime.utcnow() + timedelta(self.cleaned_data['time1']))
        send_massage.delay(self.cleaned_data['subject'], self.cleaned_data['message'])
