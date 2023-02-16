from django import forms


class Side_of_triangleForm(forms.Form):
    fvalue = forms.IntegerField(label="First cathetuse", max_value=100, min_value=1)
    svalue = forms.IntegerField(label="Second cathetuse", max_value=100, min_value=1)
