from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('triangle/', views.TriangleView, name='triangle')
]