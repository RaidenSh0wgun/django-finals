from django.shortcuts import render
from rest_framework import generics, permissions
from .models import WorkoutPlan, progressReport, Distance, Location
from .serializers import WorkoutPlanSerializer, progressReportSerializer, DistanceSerializer, LocationSerializer

# Create your views here.
class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutPlan.objects.all()

class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutPlan.objects.all()

class progressReportListCreateView(generics.ListCreateAPIView):
    serializer_class = progressReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = progressReport.objects.all()

class DistanceListCreateView(generics.ListCreateAPIView):
    serializer_class = DistanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Distance.objects.all()

class LocationListCreateView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()