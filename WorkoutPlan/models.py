from django.db import models

# Create your models here.
class WorkoutPlan(models.Model):
    WorkoutPlan = models.ManyToManyField('Exercise', related_name='workout_plans', blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    workout_plan = models.ManyToManyField(WorkoutPlan, related_name='exercises', blank=True)
    name = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField(help_text="Rest time in seconds")
    Workout_list_choices = [
        ('Pullup', 'Pullup'),
        ('Pushup', 'Pushup'),
        ('Plank', 'Plank'),
        ('Squat', 'Squat'),
        ('Lunges', 'Lunges'),
        ('Jumping Jacks', 'Jumping Jacks'),
        ('High Knees', 'High Knees'),
        ('Mountain Climbers', 'Mountain Climbers'),
        ('Sit-ups', 'Sit-ups'),
        ('Leg Raises', 'Leg Raises'),
    ]
    
    Workout_list = models.CharField(max_length=50, choices=Workout_list_choices, null=True)
    calories_burned = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.sets} sets of {self.reps} reps)"

class Location(models.Model):
    WorkoutPlan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='location_reports')
    from_location = models.CharField(max_length=200, blank=True, null=True)
    to_location = models.CharField(max_length=200, blank=True, null=True)
    Coordinates = models.CharField(max_length=50, blank=False, null=False, default='0,0')

    def __str__(self):
        try:
            return f"Location for {self.WorkoutPlan.name}"
        except Exception:
            return "Location"

class Distance(models.Model):
    WorkoutPlan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='distance_reports')
    distance_in_km = models.FloatField()

    def __str__(self):
        try:
            return f"Distance for {self.WorkoutPlan.name}: {self.distance_in_km} km"
        except Exception:
            return "Distance"

class progressReport(models.Model):
    WorkoutPlan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='progress_reports')
    progress_percentage = models.FloatField()

    def __str__(self):
        try:
            return f"Progress for {self.WorkoutPlan.name}: {self.progress_percentage}%"
        except Exception:
            return "Progress Report"
