from django.shortcuts import render
from django.views import generic


def view(request):
    template_name = 'garden_gui/index.html'
    return render(request, template_name)
