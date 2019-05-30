from django.test import TestCase
from .models import Ticket
from django.contrib.auth.models import User

# Create your tests here.
class TicketTests(TestCase):
    """ Tests for the Ticket model """
    
    # Setting up test database and logging test user in before executing tests
    def setUp(self):
        bug = Ticket.objects.create(title="Example bug",
                        summary="This is a test summary for a bug",
                        ticket_type='Bug',
                        creator='ticket_tester',
                        category='Test Category'
                    ).save()
        feature_request = Ticket.objects.create(title="Test Feature Request",
                                    summary="This is a test feature request that I would like to suggest",
                                    ticket_type='Feature Request',
                                    creator='ticket_tester',
                                    category='Test Category'
                                ).save()
        user = User.objects.create(email="ticket_test_email@test.com",
                    username="ticket_tester",
                    first_name='Tester',
                    last_name='McTestface',
                    password1='testing123',
                    password2='testing123'
                    ).save()
    
    # Ensure created tickets render on all tickets page
    def test_bug_rendered(self):
        response = self.client.get('/tickets/')
        self.assertInHTML("Example bug", response.content)
        
        
        
        
# title = models.CharField(max_length=254, default='', blank=False)
# summary = models.TextField(blank=False)
# ticket_type = models.CharField(max_length=30, blank=False)
# screenshot = models.ImageField(upload_to="images", blank=True, null=True)
# upvotes = models.IntegerField(default=0)
# total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
# creator = models.CharField(max_length=150, blank=False) 
# category = models.CharField(max_length=30, default='', blank=False)
# status = models.CharField(max_length=30, default='Backlog')
# initiation_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
# completion_date = models.DateTimeField(blank=True, null=True)