from django.test import TestCase
from io import StringIO
from django.core.management import call_command

# Create your tests here.


class CreatePromoTest(TestCase):

    def test_output(self):
        out = StringIO()
        call_command('generatepromo', 10, 'агенства', stdout=out)
        self.assertIn(f"Successfully", out.getvalue())

    