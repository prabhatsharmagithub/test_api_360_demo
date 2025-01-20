from rest_framework import serializers
from .models import project_summary, Scheme, State, Organizations


class ProjectSummarySerializer(serializers.ModelSerializer):
    scheme_name = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    # haqdarshak_state = serializers.SerializerMethodField()
    class Meta:
        model = project_summary
        fields= ['project_name','project_status', 'project_start_date', 'project_end_date', 'scheme_name','state']

    def get_scheme_name(self, obj):
        # Manually get the related Scheme by matching pid (project_summary) and project_id (Scheme)
        try:
            scheme = Scheme.objects.get(project_id=obj.pid)  # Matching project_id in Scheme to pid in project_summary
            return scheme.scheme_name
        except Scheme.DoesNotExist:
            return None  # Return None if no matching Scheme is found

    def get_state(self, obj):
        # Manually get the related State by matching pid in project_summary to organizations
        try:
            org = Organizations.objects.get(pid=obj.pid)  # Fetch organization by pid
            location = State.objects.get(id=org.location_id)  # Fetch location by location_id
            return location.state  # Return the state from the location
        except (Organizations.DoesNotExist, State.DoesNotExist):
            return None  # Return None if no matching state or organization is found