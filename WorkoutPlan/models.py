from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans', null=True, blank=True)
    exercises = models.ManyToManyField('Exercise', related_name='workout_plans', blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    rest_time = models.PositiveIntegerField(help_text="Rest time in seconds")
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
    
    Workout_list = models.CharField(max_length=50, choices=Workout_list_choices, null=True, blank=True)
    calories_burned = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.sets} sets of {self.reps} reps)"

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations', null=True, blank=True)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='location_reports')
    from_location = models.CharField(max_length=200, blank=True, null=True)
    to_location = models.CharField(max_length=200, blank=True, null=True)
    coordinates = models.CharField(max_length=50, blank=False, null=False, default='0,0')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"Location for {self.workout_plan.name}"

class Distance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='distances', null=True, blank=True)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='distance_reports')
    distance_in_km = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"Distance for {self.workout_plan.name}: {self.distance_in_km} km"

class CompletedExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_exercises')
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='completed_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='completions')
    completed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'workout_plan', 'exercise']
        ordering = ['-completed_at']

    def __str__(self):
        return f"{self.user.username} completed {self.exercise.name} in {self.workout_plan.name}"

class ProgressReport(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='progress_reports')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_reports', null=True, blank=True)
    progress_percentage = models.FloatField(editable=False, default=0.0)

    class Meta:
        unique_together = ['user', 'workout_plan']
        ordering = ['-id']
    
    def calculate_progress(self):
        if not self.user or not self.workout_plan:
            return 0.0
        
        total_exercises = self.workout_plan.exercises.count()
        
        if total_exercises == 0:
            return 0.0
        
        completed_exercises = CompletedExercise.objects.filter(
            user=self.user,
            workout_plan=self.workout_plan
        ).values('exercise').distinct().count()
        
        percentage = (completed_exercises / total_exercises) * 100
        return round(percentage, 2)
    
    def save(self, *args, **kwargs):
        self.progress_percentage = self.calculate_progress()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Progress for {self.user.username} - {self.workout_plan.name}: {self.progress_percentage}%"
