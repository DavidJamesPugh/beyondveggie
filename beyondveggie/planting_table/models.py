from django.db import models
from datetime import datetime, timedelta


class Plant(models.Model):
    """
    Initialising Plant class for use in the website.
    """
    plant_name = models.CharField(max_length=20)
    # Herb, Vegetable, or Flower
    plant_type = models.CharField(max_length=20, default='Vege')
    # Time needed in the seeder before planting in the plot
    seeding_time = models.IntegerField(default=28)
    # Time when the plant should be in the garden plot
    planting_date = models.DateField(default='2020-01-01')
    # Spacing needed for each vegetable
    plant_spacing = models.IntegerField(default=30)
    # Time needed to fully mature
    days_till_harvest = models.IntegerField(default=60)
    # Calories per harvest average
    calories = models.IntegerField(default=100)
    # Average yield per plant in grams
    yield_size = models.IntegerField(default=0)

    def __str__(self):
        return self.plant_name

    def harvest_date(self):
        # Returns a date in the future if a given plant is planted today
        harvest = datetime.now() + timedelta(days=self.days_till_harvest)
        return format(harvest, '%B %d, %Y')

    def seed_by_date(self):
        # Returns a date before a given plants' planting date.
        seeder_in_ground = self.planting_date - timedelta(days=self.seeding_time)
        return format(seeder_in_ground, '%B %d, %Y')
