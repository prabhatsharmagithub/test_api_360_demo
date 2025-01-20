from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import project_kpi, leaderboard
from .serializer import ProjectKPISerializer, AggregatedProjectKPISerializer, Projecttop5states
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Sum
from django.http import JsonResponse
from .filters import ProjectKPIFilter
from django.shortcuts import render
from django.db.models import F
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from itertools import groupby
from rest_framework.viewsets import ViewSet
from . import filters


class ProjectKPIViewSet(viewsets.ModelViewSet):
    # citizen_state = 'Haryana'
    queryset = project_kpi.objects.all()
    # queryset1 = project_kpi.objects.filter(citizen_state=citizen_state).exists
    # queryset2 = project_kpi.objects.filter(project_name=project_name).exists
    # queryset3 = project_kpi.objects.filter(scheme_name=scheme_name).exists
        
    serializer_class = ProjectKPISerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectKPIFilter

    def get_queryset(self):
        # Optionally you can modify this if you want to add more complex filtering logic
        queryset = super().get_queryset()
        return queryset

@api_view(['GET'])
def get_project_kpi(request):
    # Check if the request asks for aggregated data
    aggregated = request.GET.get('aggregated', None)
    aggregated_data = project_kpi.objects.values('project_id') \
            .annotate(
                Application_Open_Count=Sum('Application_Open_Count'),
                Docket_Submitted_Count=Sum('Docket_Submitted_Count'),
                Benefit_Received_Count=Sum('Benefit_Received_Count'),
                scheme_value=Sum('scheme_value')
            )
    # aggregated_data = project_kpi.objects.filter(project_id='project_id').all()

    # Serialize the aggregated data
    serializer = AggregatedProjectKPISerializer(aggregated_data, many=True)
    return Response(serializer.data)


class BestPerformance(APIView):
    # @action(detail=False, methods=['get'], url_path='best')
    def get(self, request):
        top_n = int(request.query_params.get('top', 5))  # Default top 5
        best_performance = (
            leaderboard.objects.values('citizen_state')
            .annotate(total_applications=Sum('application_open_count'))
            .order_by('-total_applications')[:top_n]
        )
        return Response({"best_performance": best_performance})


class BottomPerformance(APIView):
    # @action(detail=False, methods=['get'], url_path='bottom')
    def get(self, request):
        top_n = int(request.query_params.get('top', 5))  # Default bottom 5
        bottom_performance = (
            leaderboard.objects.values('citizen_state')
            .annotate(total_applications=Sum('application_open_count'))
            .order_by('total_applications')[:top_n]
        )
        return Response({"bottom_performance": bottom_performance})