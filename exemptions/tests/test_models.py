from django.test import TestCase
from exemptions.models import User, Host, Exemption
from django.core import exceptions
from django.utils import timezone
import datetime

class TestUser(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        super(TestUser, self).setUp()
        self.valid_full = User.objects.get(pk=1)
        self.valid_no_initial = User.objects.get(pk=2)
        self.lower_name = User.objects.get(pk=3)

    def test_full_name_initial(self):
        self.assertTrue(self.valid_full.full_name() == "John Q. Doe") 
        self.assertTrue(self.valid_no_initial.full_name() == "John Doe") 

    def test_lowercase_initial(self):
        self.lower_name.save()
        self.assertTrue(self.lower_name.initial == \
            self.lower_name.initial.upper())
        self.assertTrue(self.lower_name.first_name[0] == \
            self.lower_name.first_name[0].upper())
        self.assertTrue(self.lower_name.last_name[0] == \
            self.lower_name.last_name[0].upper())

class TestHost(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        super(TestHost, self).setUp()
        self.no_unique_id = Host.objects.get(pk=1)
        self.unique_id = Host.objects.get(pk=2)
        # fixture load process doesn't call this
        self.no_unique_id.save()
        self.unique_id.save()

    def test_unique_id(self):
        self.assertTrue(self.no_unique_id.unique_id == self.no_unique_id.name) 
        self.assertTrue(self.unique_id.unique_id == 'foo') 

class TestExemption(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        super(TestExemption, self).setUp()
        self.exemption = Exemption.objects.get(pk=1)
        self.host = Host.objects.get(pk=1)
        self.user = User.objects.get(pk=1)

    def test_expiration(self):
        self.assertTrue(self.exemption.expired())
        self.assertRaises(exceptions.ValidationError, self.exemption.save)

    def test_host_relation(self):
        hosts = self.exemption.hosts.all()
        self.assertTrue(len(hosts) == 1)
        self.assertTrue(hosts[0].name == self.host.name)
        self.assertTrue(hosts[0].ip == self.host.ip)
        self.assertTrue(hosts[0].pk == self.host.pk)

    def test_user_relation(self):
        user = self.exemption.requestor
        self.assertTrue(user == self.user)
        self.assertTrue(user.pk == self.user.pk)
