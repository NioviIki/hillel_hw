from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('triangle/', views.TriangleView, name='triangle'),
    path('person/', views.PersonViev, name='peron'),
    path('person/<int:id>/', views.PersikViev, name='persik')
]
