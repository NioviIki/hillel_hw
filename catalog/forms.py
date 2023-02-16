from django import forms

class TestikForm(forms.Form):
    fvalue = forms.IntegerField(label="First number", max_value=100)
    svalue = forms.IntegerField(label="Second number", max_value=100)
