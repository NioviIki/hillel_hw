from django.shortcuts import render
from math import sqrt
from .forms import TestikForm

def TriangleView(request):

    gip = None
    q_form = TestikForm()

    if TestikForm(request.GET).is_valid():
        x = list(request.GET.dict().values())
        gip = int(sqrt(int(x[0]) ** 2 + int(x[1]) ** 2))

    return render(request, 'catalog/Triangle.html', {'gip': gip, "q_form": q_form})
