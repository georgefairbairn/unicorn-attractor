from django.conf.urls import url, include
from .views import all_tickets, upvote, ticket_detail, create_bug, create_feature_request, edit_ticket

urlpatterns = [
    url(r'^$', all_tickets, name='index'),
    url(r'^upvote/(?P<pk>\d+)$', upvote, name='upvote'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    url(r'^create/bug$', create_bug, name='create_bug'),
    url(r'^create/feature-request$', create_feature_request, name='create_feature_request'),
    url(r'^edit/(?P<pk>\d+)$', edit_ticket, name='edit_ticket'),
]