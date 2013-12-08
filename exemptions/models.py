from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
import logging
from exemptions.validators import validate_not_in_past

LOG = logging.getLogger(__name__)

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False,
        verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, blank=False,
        verbose_name='Last Updated')

    class Meta:
        abstract = True

# See ``http://www.xormedia.com/django-model-validation-on-save``
class ValidateOnSaveMixin(object):
    # Because Django doesn't validate on calls to ``save`` by default..
    # ( WTF? )
    def save(self, force_insert=False, force_update=False, **kwargs):
        if not (force_insert or force_update):
            self.full_clean()
        super(ValidateOnSaveMixin, self).save(force_insert, force_update,
                                              **kwargs)

class ModelBase(ValidateOnSaveMixin, TimestampedModel):
    class Meta:
        abstract = True

class Authority(ModelBase):
    first_name = models.CharField(max_length=255, blank=False)
    initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name_plural = 'authorities'

    def save(self):
        self.initial = self.initial.upper()
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
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

    def __unicode__(self):
        return u"%s" % self.full_id()

class Host(ModelBase):
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

class Exemption(ModelBase):
    authority = models.ForeignKey(Authority, blank=False)
    expires = models.DateTimeField(blank=False, validators=[validate_not_in_past])
    request = models.TextField(blank=False)
    response = models.TextField(blank=False)
    hosts = models.ManyToManyField(Host)
    approved = models.BooleanField(default=False)

    def expired(self):
        return self.expires < timezone.now()
