from django.shortcuts import render
from tickets.models import Ticket



def get_charts(request):
    total_bugs = Ticket.objects.filter(ticket_type='Bug').count()
    total_feature_requests = Ticket.objects.filter(ticket_type='Feature Request').count()
    user = request.user
    user_bugs = Ticket.objects.filter(ticket_type='Bug', creator=user).count()
    user_feature_requests = Ticket.objects.filter(ticket_type='Feature Request', creator=user).count()
    return render(request, 'charts.html', {'total_bugs': total_bugs, 
                                            'total_feature_requests': total_feature_requests,
                                            'user_bugs': user_bugs,
                                            'user_feature_requests': user_feature_requests,
                                            'user': user
    })