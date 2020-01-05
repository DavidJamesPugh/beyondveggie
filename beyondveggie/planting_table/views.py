from django.views import generic

from .models import Plant


class IndexView(generic.ListView):
    template_name = 'planting_table/index.html'
    context_object_name = 'plant_data_list'

    def get_queryset(self):
        return Plant.objects.order_by('planting_date')
