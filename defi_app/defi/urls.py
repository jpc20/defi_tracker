from django.urls import path

from . import views

app_name = 'defi'
urlpatterns = [
    path('', views.index, name='index')
]