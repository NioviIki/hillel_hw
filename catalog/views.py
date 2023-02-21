from math import sqrt

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import Person, PersonForm, Side_of_triangleForm


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

    if request.method == 'GET':
        form = PersonForm

        return render(request, 'catalog/Person.html', {"form": form})

    else:
        form = PersonForm(request.POST)

        if form.is_valid():

            form.clean()
            x = form.cleaned_data
            Person.objects.bulk_create(
                [Person(first_name=x.get('first_name'),
                        last_name=x.get('last_name'),
                        email=x.get('email'))])

            return redirect(reverse('catalog:person'))

        else:

            error_mas = "Incorrect inputi"

            return render(request, 'catalog/Person.html', {"error_mas": error_mas})


def GetPersonViev(request, person_id):
    my_object = get_object_or_404(Person, pk=person_id)

    if request.method == "GET":
        form = PersonForm(instance=my_object)
        return render(request, 'catalog/GetPerson.html', {'x': my_object, "form": form})

    else:

        form = PersonForm(request.POST)

        if form.is_valid():

            form.clean()
            x = form.cleaned_data
            data_to_update = Person.objects.filter(pk=person_id)
            data_to_update.update(first_name=x.get('first_name'))
            data_to_update.update(last_name=x.get('last_name'))
            data_to_update.update(email=x.get('email'))

            return redirect(reverse('catalog:GetPerson', args=(person_id,)))

        else:
            error_mas = "Incorrect input"

            return render(request, 'catalog/Person.html', {"error_mas": error_mas})
