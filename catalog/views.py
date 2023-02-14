from django.shortcuts import render
from math import sqrt
from .forms import TestikForm

def TriangleView(request):

    gip = None
    q_form = TestikForm(request.POST)
    list_of_side = request.GET.getlist('q_form')

    if list_of_side:
        gip = int(sqrt(int(list_of_side[0]) ** 2 + int(list_of_side[1]) ** 2))

    return render(request, 'catalog/Triangle.html', {'gip': gip, "q_form": q_form, })
