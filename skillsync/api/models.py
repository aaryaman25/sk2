from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_id = models.CharField(max_length=50, unique=True, null=True)
    business_title = models.CharField(max_length=100)
    salary_range_from = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    salary_range_to = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    work_location = models.CharField(max_length=100, null=True)
    posting_date = models.DateField(null=True)
    job_description = models.TextField(null=True)
    closing_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.business_title
    
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
