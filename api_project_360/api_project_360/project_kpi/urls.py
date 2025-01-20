from django.contrib import admin
from django.urls import path, include
from .views import get_project_kpi
from rest_framework.routers import DefaultRouter
from .views import ProjectKPIViewSet 
#top_ranked_applications
from . import views
# from .views import LeaderboardViewSet
from .views import BestPerformance
from .views import BottomPerformance


router = DefaultRouter()
router.register(r'project_kpi', ProjectKPIViewSet)

urlpatterns = [
    path('project_kpi/', get_project_kpi, name='get_project_kpi'), 
    path('best/', BestPerformance.as_view(), name='get_best_performance'),
    path('bottom/', BottomPerformance.as_view(), name='get_bottom_performance'),
]