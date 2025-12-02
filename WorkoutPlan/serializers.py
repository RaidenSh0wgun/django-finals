from .models import WorkoutPlan, progressReport, Distance, Location
from rest_framework import serializers


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = '__all__'

class progressReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = progressReport
        fields = '__all__'