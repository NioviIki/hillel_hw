from django import forms
from django.forms import ModelForm

from .models import Person


class Side_of_triangleForm(forms.Form):
    fvalue = forms.IntegerField(label="First cathetuse", max_value=100, min_value=1)
    svalue = forms.IntegerField(label="Second cathetuse", max_value=100, min_value=1)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "email")
        labels = {
            'first_name': "First name",
            'last_name': "Last name",
            'email': "Email"
        }
