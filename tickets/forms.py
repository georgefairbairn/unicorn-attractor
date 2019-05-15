from django import forms
from .models import Ticket, Comment

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'summary', 'ticket_type', 'category', 'screenshot')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)