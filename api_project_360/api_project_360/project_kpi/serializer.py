from rest_framework import serializers
from .models import project_kpi
from django.db.models import Sum
from rest_framework.response import Response

class ProjectKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = project_kpi
        fields = ['project_id','Application_Open_Count','Docket_Submitted_Count','Benefit_Received_Count','scheme_value'] 


# Serializer to return aggregated data
class AggregatedProjectKPISerializer(serializers.Serializer):
    project_id = serializers.CharField()
    # citizen_state = serializers.CharField()
    Application_Open_Count = serializers.IntegerField()
    Docket_Submitted_Count = serializers.IntegerField()
    Benefit_Received_Count = serializers.IntegerField()
    scheme_value = serializers.IntegerField()


class Projecttop5states(serializers.Serializer):
    state_name = serializers.CharField()
    Application_Open = serializers.IntegerField()
