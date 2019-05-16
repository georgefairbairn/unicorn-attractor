from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from .models import Ticket
from .forms import TicketForm, PaymentForm
from comments.models import Comment
from comments.forms import CommentForm
import stripe

stripe.api_key = settings.STRIPE_SECRET

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
def create_bug(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = Ticket(title=form.cleaned_data['title'],
                            summary=form.cleaned_data['summary'],
                            ticket_type='Bug',
                            screenshot=form.cleaned_data['screenshot'],
                            creator=request.user,
                            category=form.cleaned_data['category'],
                            initiation_date=timezone.now())
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'create-bug.html', {'form': form})
    
    
@login_required
def create_feature_request(request):
    if request.method=="POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        payment_form = PaymentForm(request.POST)
        
        if ticket_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(amount = 5000,
                                                currency = "GBP",
                                                description = request.user.email,
                                                card = payment_form.cleaned_data['stripe_id'],
                                                )
            except:
                messages.error(request, "Your card was declined")
                
            if customer.paid:
                messages.error(request, "Your payment was successful")
                ticket = Ticket(title=ticket_form.cleaned_data['title'],
                                summary=ticket_form.cleaned_data['summary'],
                                ticket_type='Feature Request',
                                total_paid = customer.amount / 100,
                                screenshot=ticket_form.cleaned_data['screenshot'],
                                creator=request.user,
                                category=ticket_form.cleaned_data['category'],
                                initiation_date=timezone.now())
                ticket.save()
                return redirect(ticket_detail, ticket.id)
                
            else:
                messages.error(request, "Unable to take payment")
        
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card")
            
    else:
        ticket_form = TicketForm()
        payment_form = PaymentForm()
        
    return render(request, "create-feature-request.html", {'ticket_form': ticket_form, 
                                            'payment_form': payment_form,
                                            'publishable': settings.STRIPE_PUBLISHABLE})
                                            
                                            
@login_required
def edit_ticket(request, pk=None, ttype=None):
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