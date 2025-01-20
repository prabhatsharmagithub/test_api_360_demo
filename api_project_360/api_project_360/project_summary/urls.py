from django.contrib import admin
from django.urls import path, include
from .views import get_project_summary
from .views import ProjectSummaryViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'project_summary', ProjectSummaryViewSet)

urlpatterns = [
    path('project_summary/', views.get_project_summary, name='get_project_summary'), 
    path('state_choices/', views.get_state_choices, name='state_choices'),
    path('project_name_choices/', views.get_project_name_choices, name='project_name_choices'),
    path('scheme_name_choices/', views.get_scheme_name_choices, name='scheme_name_choices'),
]


# urlpatterns = [
#     path('state_choices/', views.get_state_choices, name='state_choices'),
#     path('project_name_choices/', views.get_project_name_choices, name='project_name_choices'),
#     path('scheme_name_choices/', views.get_scheme_name_choices, name='scheme_name_choices'),
# ]
