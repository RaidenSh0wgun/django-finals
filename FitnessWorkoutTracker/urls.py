"""
URL configuration for FitnessWorkoutTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Goal.views import GoalListCreateView, GoalDetailView
from WorkoutPlan.views import WorkoutPlanListCreateView, WorkoutPlanDetailView, ProgressReportListCreateView, DistanceListCreateView, LocationListCreateView, CompletedExerciseCreateView, CompletedExerciseListView, ExerciseListCreateView, ExerciseDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import UserProfileView, UserProfileListView, LeaderboardView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/user-profiles/', UserProfileListView.as_view(), name='user-profiles'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('api/goals/', GoalListCreateView.as_view(), name='goal-list-create'),
    path('api/goals-detail/', GoalDetailView.as_view(), name='goal-detail'),
    path('api/progress-reports/', ProgressReportListCreateView.as_view(), name='progress-report-list-create'),
    path('api/completed-exercises/', CompletedExerciseCreateView.as_view(), name='completed-exercise-create'),
    path('api/completed-exercises/list/', CompletedExerciseListView.as_view(), name='completed-exercise-list'),
    path('api/locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('api/distances/', DistanceListCreateView.as_view(), name='distance-list-create'),
    path('api/workout-plans/', WorkoutPlanListCreateView.as_view(), name='workout-plan-list-create'),
    path('api/workout-plans-details/', WorkoutPlanDetailView.as_view(), name='workout-plan-detail'),
    path('api/exercises/', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('api/exercises-detail/', ExerciseDetailView.as_view(), name='exercise-detail'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

