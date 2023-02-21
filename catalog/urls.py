from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('triangle/', views.TriangleView, name='triangle'),
    path('person/', views.PersonViev, name='person'),
    path('person/<int:person_id>/', views.GetPersonViev, name='GetPerson')
]
