from django.contrib import admin
from .models import Exercise, WorkoutPlan, Location, Distance, ProgressReport, CompletedExercise

class WorkoutPlanAdmin(admin.ModelAdmin):
    filter_horizontal = ('exercises',)
    list_display = ('name', 'user', 'created_at')
    list_filter = ('created_at', 'user')

class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout_plan', 'progress_percentage')
    list_filter = ('user', 'workout_plan')

admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(Exercise)
admin.site.register(Location)
admin.site.register(Distance)
admin.site.register(ProgressReport, ProgressReportAdmin)
admin.site.register(CompletedExercise)