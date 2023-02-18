from math import sqrt

from django.shortcuts import render

from .forms import Side_of_triangleForm, PersonForm


def TriangleView(request):

    hip = None
    form = Side_of_triangleForm(request.GET)

    if form.is_valid():
        cathetuses_of_triangle = list(request.GET.dict().values())
        hip = int(sqrt(int(cathetuses_of_triangle[0]) ** 2 +
                       int(cathetuses_of_triangle[1]) ** 2))

    return render(request, 'catalog/Triangle.html',
                  {'hip': hip, "q_form": Side_of_triangleForm(), "form": form})

def PersonViev(request):
    form = PersonForm

    return render(request, 'catalog/Person.html', {"form": form})

def PersikViev(request, id):

    return render(request, 'catalog/Person.html', {'id': id})