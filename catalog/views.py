from django.shortcuts import render
from math import sqrt
from .forms import TestikForm

def TestikView(request):

    gip = None
    fvalue = TestikForm(request.POST)
    svalue =  TestikForm(request.POST)
    fnumber, snumber = request.GET.getlist('fvalue'), request.GET.getlist('svalue')

    if fnumber and snumber:
        gip = int(sqrt(int(fnumber[0]) ** 2 + int(snumber[0]) ** 2))

    return render(request, 'catalog/test.html', {"fnumber": fnumber,
                                                 "snumber": snumber,
                                                 'gip': gip,
                                                 "fvalue": fvalue,
                                                 'svalue': svalue,
                                                 "testik": testik
                                                 })
