from django.urls import path
from . import views

app_name = 'garden_gui'

urlpatterns = [
    path('', views.view, name='index')


]
