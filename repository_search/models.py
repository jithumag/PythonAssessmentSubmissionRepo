from django.db import models
from django.utils import timezone

class Repository(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    owner = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(null=True,blank=True)
    stars = models.IntegerField(null=True,blank=True)
    forks = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
