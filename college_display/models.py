from django.db import models

class PriceRange(models.Model):
    range = models.CharField(max_length=255)

    def __str__(self):
        return self.range
    
class Activity(models.Model):
    club = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='Miscellaneous')
    def __str__(self):
        return self.club
    

class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class College(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255, blank=True)
    activities = models.ManyToManyField(Activity, related_name='schools_activities', blank=True)
    majors = models.ManyToManyField(Major, related_name='schools_majors', blank=True)
    population = models.BigIntegerField()
    class_size = models.BigIntegerField()
    location = models.CharField(max_length=255)
    atmosphere = models.CharField(max_length=255)
    crime_rate = models.CharField(max_length=255)
    faith_life = models.CharField(max_length=255)
    link = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name