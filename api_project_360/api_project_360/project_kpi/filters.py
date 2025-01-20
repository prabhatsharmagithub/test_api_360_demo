import django_filters
from .models import project_kpi

class ProjectKPIFilter(django_filters.FilterSet):
    project_id = django_filters.CharFilter(lookup_expr='icontains', label='Project ID')

    class Meta:
        model = project_kpi
        fields = ['project_id']