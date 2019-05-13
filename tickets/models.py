from django.db import models
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=254, default='')
    summary = models.TextField()
    ticket_type = models.CharField(max_length=30)
    screenshot = models.ImageField(upload_to="images", blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    category = models.CharField(max_length=30, default='')
    status = models.CharField(max_length=30, default='Backlog')
    initiation_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    completion_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    