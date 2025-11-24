from django.contrib import admin
from .models import Exercise, WorkoutPlan, Location

# Register your models here.
admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
admin.site.register(Location)