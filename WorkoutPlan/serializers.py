from .models import WorkoutPlan, ProgressReport, Distance, Location, CompletedExercise, Exercise
from rest_framework import serializers


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(many=True, queryset=Exercise.objects.all(), required=False)
    exercise_details = ExerciseSerializer(source='exercises', many=True, read_only=True)
    
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
        read_only_fields = ('user', 'created_at')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('user',)

class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = '__all__'
        read_only_fields = ('user',)

class CompletedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedExercise
        fields = '__all__'
        read_only_fields = ('user', 'completed_at')

class ProgressReportSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = ProgressReport
        fields = '__all__'
        read_only_fields = ('user', 'progress_percentage')