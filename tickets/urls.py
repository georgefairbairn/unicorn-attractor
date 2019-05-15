from django.conf.urls import url, include
from .views import all_tickets, upvote, ticket_detail, create_or_edit_ticket, create_comment

urlpatterns = [
    url(r'^$', all_tickets, name='index'),
    url(r'^upvote/(?P<pk>\d+)$', upvote, name='upvote'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    url(r'^new/$', create_or_edit_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket'),
    url(r'^comment/(?P<pk>\d+)$', create_comment, name='create_comment')
]