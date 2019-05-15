from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm

# Create your views here.
def all_tickets(request):
    tickets = Ticket.objects.all()
    comments = Comment.objects.all()
    comment_form = CommentForm()
    return render(request, 'tickets.html', {'tickets': tickets, 'comments': comments, 'comment_form': comment_form})
    

@login_required    
def upvote(request, pk, called_from):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.save()
    return redirect(reverse('index'))
    
    
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket-detail.html', {'ticket': ticket})
    

@login_required
def create_or_edit_ticket(request, pk=None):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    edit_state = True
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = Ticket(title=form.cleaned_data['title'],
                            summary=form.cleaned_data['summary'],
                            ticket_type=form.cleaned_data['ticket_type'],
                            screenshot=form.cleaned_data['screenshot'],
                            creator=request.user,
                            category=form.cleaned_data['category'],
                            initiation_date=timezone.now())
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        if pk == None:
            edit_state = False
        form = TicketForm(instance=ticket)
    return render(request, 'create-ticket.html', {'form': form, 'edit_state': edit_state})
    
    
@login_required
def create_comment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            comment = Comment(ticket=ticket,
                                user=request.user,
                                comment=form.cleaned_data['comment'],
                                comment_date=timezone.now())
            comment.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = CommentForm(instance=ticket)
    return redirect(all_tickets)