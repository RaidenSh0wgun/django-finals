from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import WorkoutPlan, ProgressReport, Distance, Location, CompletedExercise, Exercise
from .serializers import WorkoutPlanSerializer, ProgressReportSerializer, DistanceSerializer, LocationSerializer, CompletedExerciseSerializer, ExerciseSerializer

class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutPlan.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to create a workout plan.")
        serializer.save(user=self.request.user)

class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkoutPlan.objects.all()

class ProgressReportListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgressReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProgressReport.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to create a progress report.")
        serializer.save(user=self.request.user)

class CompletedExerciseCreateView(generics.CreateAPIView):
    serializer_class = CompletedExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to log a completed exercise.")
        serializer.save(user=self.request.user)

class CompletedExerciseListView(generics.ListAPIView):
    serializer_class = CompletedExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CompletedExercise.objects.filter(user=self.request.user)

class DistanceListCreateView(generics.ListCreateAPIView):
    serializer_class = DistanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Distance.objects.all()

class DistanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DistanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Distance.objects.all()

class LocationListCreateView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to create a location.")
        serializer.save(user=self.request.user)

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()

class ExerciseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()

class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()