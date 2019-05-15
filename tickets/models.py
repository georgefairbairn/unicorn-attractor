from django.db import models
from django.utils import timezone

type_choices = [
    ('Bug', 'Bug'),
    ('Feature Request', 'Feature Request')
]

# Create your models here.
class Ticket(models.Model):
    
    title = models.CharField(max_length=254, default='', blank=False)
    summary = models.TextField(blank=False)
    ticket_type = models.CharField(max_length=30, choices=type_choices, blank=False)
    screenshot = models.ImageField(upload_to="images", blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    creator = models.CharField(max_length=254, blank=False) 
    category = models.CharField(max_length=30, default='', blank=False)
    status = models.CharField(max_length=30, default='Backlog')
    initiation_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    completion_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    
    ticket = models.ForeignKey(Ticket, null=False)
    author = models.CharField(max_length=254, blank=False)
    comment = models.TextField(blank=False)
    comment_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    
    def __str__(self):
        return "Comment {0} by {1} (Ticket {2})".format(self.id, self.author, self.ticket.title)
    
    
    