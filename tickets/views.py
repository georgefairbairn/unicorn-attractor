from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm

# Create your views here.
def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})
    
    
def upvote(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.save()
    return redirect(reverse('tickets'))
    
    
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket-detail.html', {'ticket': ticket})
    
    
def create_or_edit_ticket(request, pk=None):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'create-ticket.html', {'form': form})