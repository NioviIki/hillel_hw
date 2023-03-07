from django.shortcuts import render

from .forms import TForm


def email_feedback(request):
    forms = TForm
    if request.method == "POST":
        form = TForm(request.POST)
        if form.is_valid():
            form.send_massages()
            return render(request, 'send_email/email_feedback.html', {'forms': TForm})
        else:
            raise ValueError
    return render(request, 'send_email/email_feedback.html', {'forms': forms})
