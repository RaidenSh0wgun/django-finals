from django.shortcuts import render
from rest_framework import generics, permissions
from .models import WorkoutPlan
from .serializers import WorkoutPlanSerializer

# Create your views here.
class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutPlan.objects.all()

class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutPlan.objects.all()
