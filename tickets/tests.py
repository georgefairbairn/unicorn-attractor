from django.test import TestCase
from .models import Ticket

# Create your tests here.
class TicketTests(TestCase):
    """ Test for the Ticket model """
    def test_str(self):
        test_title = Ticket(title="Example ticket")
        self.assertEqual(str(test_title), " - Example ticket")