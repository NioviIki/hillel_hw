from django.urls import path

from . import views

app_name = 'send_email'

urlpatterns = [
    path('', views.tes, name='tes')
]