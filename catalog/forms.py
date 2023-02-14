from django import forms

class TestikForm(forms.Form):
    fvalue = forms.IntegerField()
    svalue = forms.IntegerField()
