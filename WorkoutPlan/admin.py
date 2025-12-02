from django.contrib import admin
from .models import Exercise, WorkoutPlan, Location, Distance, progressReport

# Register your models here.
admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
admin.site.register(Location)
admin.site.register(Distance)
admin.site.register(progressReport)