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
        ('high knees', 'high knees'),
        ('Burpees', 'Burpees'),
        ('Mountain Climbers', 'Mountain Climbers'),
        ('Sit-ups', 'Sit-ups'),
        ('Leg Raises', 'Leg Raises'),
        ('Bicycle Crunches', 'Bicycle Crunches'),
        ('Russian Twists', 'Russian Twists'),
        ('Tricep Dips', 'Tricep Dips'),
        ('Wall Sit', 'Wall Sit'),
        ('Calf Raises', 'Calf Raises'),
        ('Glute Bridges', 'Glute Bridges'),
        ('Donkey Kicks', 'Donkey Kicks'),
        ('Fire Hydrants', 'Fire Hydrants'),
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

