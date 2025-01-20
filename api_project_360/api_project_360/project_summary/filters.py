import django_filters
from .models import project_summary, Scheme, State, Organizations

class ProjectSummaryFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(field_name='project_name', lookup_expr='icontains', label='Project Name')
    state = django_filters.CharFilter(method='filter_by_state', label='State')
    scheme_name = django_filters.CharFilter(method='filter_by_scheme', label='Scheme Name')

    class Meta:
        model = project_summary
        fields = ['project_name', 'state', 'scheme_name']

    def filter_by_state(self, queryset, name, value):
        # Filter the queryset based on the state selection
        if value:
            # Get the organizations related to the selected state
            organizations = Organizations.objects.filter(location_id__in=State.objects.filter(state=value).values('id'))
            return queryset.filter(pid__in=organizations.values('pid'))
        return queryset

    def filter_by_scheme(self, queryset, name, value):
        # Filter the queryset based on the scheme_name selection, related to a specific state
        if value:
            schemes = Scheme.objects.filter(scheme_name=value)
            return queryset.filter(pid__in=schemes.values('project_id'))
        return queryset
