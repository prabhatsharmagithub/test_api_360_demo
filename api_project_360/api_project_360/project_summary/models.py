from django.db import models

# Create your models here.

class State(models.Model):
    state = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'locations'

    def __str__(self):
        return self.state


class Organizations(models.Model):
    # state = models.CharField(max_length=100)
    location_id = models.IntegerField()
    pid = models.CharField(max_length=100)

    class Meta:
        db_table = 'organizations'

    def __str__(self):
        return self.state


class Scheme(models.Model):
    scheme_name = models.CharField(max_length=100)
    project_id = models.CharField(max_length=100, unique=True, primary_key=True)

    class Meta:
        db_table = 'daily_aggregates'

    def __str__(self):
        return self.scheme_name


class project_summary(models.Model):
    project_name = models.CharField(max_length=100)
    project_status = models.CharField(max_length=100)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    pid = models.CharField(max_length=100)


    class Meta:
        db_table = 'project_management'

    def __str__(self):
        return self.project_name
    