from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import WorkoutPlan, ProgressReport, Distance, Location, CompletedExercise, Exercise
from .serializers import WorkoutPlanSerializer, ProgressReportSerializer, DistanceSerializer, LocationSerializer, CompletedExerciseSerializer, ExerciseSerializer

class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)
    
    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You don't have permission to access this workout plan.")
        return obj

class ProgressReportListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgressReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ProgressReport.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        workout_plan = serializer.validated_data['workout_plan']
        user = self.request.user
        
        if workout_plan.user != user:
            raise PermissionDenied("You can only create progress reports for your own workout plans.")
        
        progress_report, created = ProgressReport.objects.get_or_create(
            user=user,
            workout_plan=workout_plan
        )
        
        if not created:
            progress_report.save()
        
        serializer.instance = progress_report

class CompletedExerciseCreateView(generics.CreateAPIView):
    serializer_class = CompletedExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        workout_plan = serializer.validated_data['workout_plan']
        exercise = serializer.validated_data['exercise']
        
        if workout_plan.user != user:
            raise PermissionDenied("You can only complete exercises for your own workout plans.")
        
        completed_exercise, created = CompletedExercise.objects.get_or_create(
            user=user,
            workout_plan=workout_plan,
            exercise=exercise
        )
        
        serializer.instance = completed_exercise
        
        progress_report, _ = ProgressReport.objects.get_or_create(
            user=user,
            workout_plan=workout_plan
        )
        progress_report.save()

class CompletedExerciseListView(generics.ListAPIView):
    serializer_class = CompletedExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        workout_plan_id = self.request.query_params.get('workout_plan', None)
        queryset = CompletedExercise.objects.filter(user=self.request.user)
        
        if workout_plan_id:
            queryset = queryset.filter(workout_plan_id=workout_plan_id)
        
        return queryset

class DistanceListCreateView(generics.ListCreateAPIView):
    serializer_class = DistanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Distance.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        workout_plan = serializer.validated_data['workout_plan']
        if workout_plan.user != self.request.user:
            raise PermissionDenied("You can only add distances to your own workout plans.")
        serializer.save(user=self.request.user)

class LocationListCreateView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        workout_plan = serializer.validated_data['workout_plan']
        if workout_plan.user != self.request.user:
            raise PermissionDenied("You can only add locations to your own workout plans.")
        serializer.save(user=self.request.user)

class ExerciseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()

class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()