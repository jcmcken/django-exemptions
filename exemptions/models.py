from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
import logging

LOG = logging.getLogger(__name__)

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False,
        verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, blank=False,
        verbose_name='Last Updated')

    class Meta:
        abstract = True

class Authority(TimestampedModel):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    initial = models.CharField(max_length=1, blank=True)
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name_plural = 'authorities'

    def save(self):
        self.initial = self.initial.upper()
        super(Authority, self).save()

    def full_name(self):
        if self.initial:
            initial = "%s." % self.initial
        else:
            initial = ''
        full = "%s %s %s" % (self.first_name, initial, self.last_name)
        return ' '.join(full.split()) # to remove extraneous whitespace

    def full_id(self):
        return "%s <%s>" % (self.full_name(), self.email)

class Host(TimestampedModel):
    name = models.CharField(max_length=255, blank=False,
        verbose_name='Hostname')
    ip = models.GenericIPAddressField(blank=False, verbose_name='IP Address')
    unique_id = models.CharField(max_length=255, blank=True, unique=True,
        verbose_name='Unique ID')

    def save(self, *args, **kwargs):
        if not self.unique_id:
            # host's unique_id (i.e. serial #) defaults to hostname
            self.unique_id = self.name
        super(Host, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.ip)

class Exemption(TimestampedModel):
    authority = models.ForeignKey(Authority, blank=False)
    expires = models.DateTimeField(blank=False)
    request = models.TextField(blank=False)
    response = models.TextField(blank=False)
    hosts = models.ManyToManyField(Host)
    approved = models.BooleanField(default=False)

    def expired(self):
        return self.expires < timezone.now()
