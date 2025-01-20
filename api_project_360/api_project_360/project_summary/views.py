from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import project_summary, Scheme, State
from .serializer import ProjectSummarySerializer
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import ProjectSummaryFilter


@api_view(['GET'])
def get_state_choices(request):
    # Return distinct states
    states = State.objects.all().values('state')
    return Response(states)

@api_view(['GET'])
def get_project_name_choices(request):
    # Return distinct project names
    project_names = project_summary.objects.all().values('project_name').distinct()
    return Response(project_names)

@api_view(['GET'])
def get_scheme_name_choices(request):
    # Return distinct scheme names
    schemes = Scheme.objects.all().values('scheme_name').distinct()
    return Response(schemes)


# Create your views here.
@api_view(['GET'])
def get_project_summary(request):
    project_summaries = project_summary.objects.using('default').all()
    serializer = ProjectSummarySerializer(project_summaries, many=True)
    
    return Response(serializer.data)

# For project_summary, we use a viewset with filtering capabilities
class ProjectSummaryViewSet(viewsets.ModelViewSet):
    queryset = project_summary.objects.all()
    serializer_class = ProjectSummarySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectSummaryFilter  # Apply the filterset class


    def get_queryset(self):
        # modify this if you want to add more complex filtering logic
        queryset = super().get_queryset()
        return queryset

