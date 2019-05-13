from django.conf.urls import url, include
from .views import all_tickets, upvote, ticket_detail, create_or_edit_ticket

urlpatterns = [
    url(r'^$', all_tickets, name='tickets'),
    url(r'^upvote/(?P<id>\d+)$', upvote, name='upvote'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    url(r'^new/$', create_or_edit_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket'),
]