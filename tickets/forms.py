from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'summary', 'ticket_type', 'category', 'screenshot')