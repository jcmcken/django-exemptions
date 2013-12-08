from django.test import TestCase
from exemptions.forms import HostForm, UserForm, ExemptionForm
from exemptions.models import Host
from django.utils import timezone
import datetime

class TestHostForm(TestCase):
    def setUp(self):
        self.form = HostForm(data={
          'name': 'foo',
          'ip': '127.0.0.1',
          'unique_id': 'bar',
        })

    def test_initial_conditions(self):
        self.assertTrue(self.form.is_valid())

    def test_invalid_ip(self):
        self.form.data['ip'] = 'invalidipaddress' 
        self.assertFalse(self.form.is_valid())

    def test_no_unique_id(self):
        self.form.data['unique_id'] = ''
        self.assertTrue(self.form.is_valid())

    def test_invalid_name(self):
        self.form.data['name'] = (Host._meta.get_field('name').max_length + 1) * 'a'
        self.assertFalse(self.form.is_valid())

class TestUserForm(TestCase):
    def setUp(self):
        self.form = UserForm(data={
          'first_name': 'John',
          'initial': 'Q',
          'last_name': 'Doe',
          'email': 'johnqdoe@gmail.com',
        })

    def test_initial_conditions(self):
        self.assertTrue(self.form.is_valid())

    def test_no_initial(self):
        self.form.data['initial'] = ''
        self.assertTrue(self.form.is_valid())

    def test_bad_initial(self):
        self.form.data['initial'] = 'foo'
        self.assertFalse(self.form.is_valid())
    
    def test_missing_email(self):
        self.form.data['email'] = ''
        self.assertFalse(self.form.is_valid())

    def test_missing_first_name(self):
        self.form.data['first_name'] = ''
        self.assertFalse(self.form.is_valid())

    def test_missing_last_name(self):
        self.form.data['last_name'] = ''
        self.assertFalse(self.form.is_valid())

class TestExemptionForm(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.timedelta = datetime.timedelta(weeks=2)
        self.form = ExemptionForm(data={
            'requestor': 1,
            'hosts': [1],
            'expires': timezone.now() + self.timedelta,
            'request': 'foo',
            'response': 'bar',
        })

    def test_initial_conditions(self):
        self.assertTrue(self.form.is_valid())

    def test_invalid_expiration(self):
        self.form.data['expires'] = self.form.data['expires'] - (self.timedelta * 2) 
        self.assertFalse(self.form.is_valid())

