from django.contrib import admin
from .models import Plant
# Register your models here.


class PlantInLine(admin.TabularInline):
    model = Plant


class PlantAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['plant_name']}),
                 ('Days till harvest', {'fields': ['days_till_harvest']}),
                 ('Planting date', {'fields': ['planting_date']})
                 ]

    list_display = ('plant_name', 'planting_date',
                    'days_till_harvest', 'harvest_date')


admin.site.register(Plant, PlantAdmin)
