from django import forms
from django.utils import timezone

from .tasks import send_massage


class TForm(forms.Form):
    subject = forms.CharField(max_length=20, label='Subject')
    message = forms.CharField(max_length=200, label='Message', widget=forms.Textarea)
    email = forms.EmailField(label='Email')
    time1 = forms.DateTimeField(label='Time', input_formats=['%d-%m-%Y %H:%M'],
                                initial=timezone.now()
                                )

    def send_massages(self):
        now = self.cleaned_data['time1'] - timezone.now()
        now = now.seconds + (now.days * 24 * 60 * 60)
        if now < 0 or now > 172800:
            raise ValueError
        else:
            send_massage.apply_async(args=[self.cleaned_data['subject'],
                                     self.cleaned_data['message'],
                                     self.cleaned_data['email']],
                                     eta=self.cleaned_data['time1'])
