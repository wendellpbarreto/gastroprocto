#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

from .countries import CountryField

class Banner(models.Model):
    '''
    '''
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(_('Active'), default=True, help_text=_('Banner is active?'))
    image = ImageField(_('Image'), upload_to='banner/', help_text=_('Banner image'))

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')

    def __unicode__(self):
        return u'%s' % self.id

    def photo_tag(self):
        return "<img src=\"%s\"/ width=\"800px\">" % (self.image.url)

    photo_tag.short_description = _("Current photo")
    photo_tag.allow_tags = True

class Info(models.Model):
    '''
    Website informations
    '''
    confirm_payment = models.CharField(_('Confirm payment'), max_length=512, help_text=_('Confirme payment information'))
    how_to_buy = models.CharField(_('How to buy'), max_length=512, help_text=_('How to buy information'))
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Information')
        verbose_name_plural = _('Informations')

    def __unicode__(self):
        return u'Information'

class Treatment(models.Model):
    '''
    Establishment open times
    '''
    value = models.CharField(_('Treatment'), max_length=62, help_text=_('Treatment value'))
    info = models.ForeignKey(Info)

    class Meta:
        verbose_name = _('Treatment')
        verbose_name_plural = _('Treatments')

    def __unicode__(self):
        return u'%s' % (self.value.capitalize())

class Contact(models.Model):
    '''
    Info contact
    '''
    EMAIL = 'email'
    PHONE = 'phone'
    SKYPE = 'skype'
    TYPES = (
        (EMAIL, 'E-mail'),
        (PHONE, 'Phone number'),
        (SKYPE, 'Skype id'),
    )

    type = models.CharField(_('Type'), max_length=5, choices=TYPES, help_text=_('Contact type'))
    value = models.CharField(_('Value'), max_length=32, help_text=_('Contact value'))
    info = models.ForeignKey(Info)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        return u'%s contact' % (self.type.capitalize())

class Bank(models.Model):
    '''
    Available bank to deposit or money transfer
    '''
    name = models.CharField(_('Name'), max_length=32, help_text=_('Bank name'))
    observation = models.TextField(_('Observation'), max_length=512, blank=True, help_text=_('Bank observation'))
    image = models.ImageField(upload_to='/media/bank/')

    class Meta:
        verbose_name = _('Bank')
        verbose_name_plural = _('Banks')

    def __unicode__(self):
        return u'%s' % (self.name.capitalize())

class Account(models.Model):
    '''
    Account for deposit or money transfer
    '''
    CHECKING = 'checking'
    SAVING = 'saving'
    TYPES = (
        (CHECKING, 'Checking account'),
        (SAVING, 'Saving account'),
    )

    agency = models.CharField(_('Agency'), max_length=16, help_text=_('Account agency'))
    account = models.CharField(_('Account'), max_length=16, help_text=_('Account'))
    operation = models.CharField(_('Operation'), max_length=16, blank=True, help_text=_('Account operation'))
    owner = models.CharField(_('Owner'), max_length=32, help_text=_('Account owner'))
    type = models.CharField(_('Type'), max_length=16, choices=TYPES, help_text=_('Account type'))
    bank = models.ForeignKey(Bank)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __unicode__(self):
        return u'Bank %s account' % (self.bank.name.capitalize())

class Bot(models.Model):
    '''
    Bot
    '''
    name = models.CharField(_('Name'), max_length=32, help_text=_('Bot name'))
    subtitle = models.CharField(_('Subtitle'), max_length=128, help_text=_('Bot subtitle'))
    observation = models.TextField(_('Observation'), max_length=512, blank=True, help_text=_('Bot observation'))
    image = models.ImageField(upload_to='/media/bot/')

    class Meta:
        verbose_name = _('Bot')
        verbose_name_plural = _('Bots')

    def __unicode__(self):
        return u'Bot'

class Nationality(models.Model):
    '''
    '''
    name = models.CharField(_('nationality'), max_length=64, help_text=_('Nationality'))
    country = CountryField()

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationalities')

    def __unicode__(self):
        return u'%s' % (self.name.upper())

class Server(models.Model):
    '''
    '''
    ORIGINAL = 'original'
    PRIVATE = 'private'
    ORIGINALITY = (
        (ORIGINAL, 'Original'),
        (PRIVATE, 'Private')
    )

    name = models.CharField(_('name'), max_length=32, help_text=_('Server name'))
    description = models.TextField(_('description'), max_length=1024, help_text=_('Description'))
    originality = models.CharField(_('originality'), max_length=8, choices=ORIGINALITY, help_text=_('Originality'))
    nationality = models.ForeignKey(Nationality, verbose_name=_('nationality'), help_text=_('Server nationality'))
    cap = models.CharField(_('cap'), max_length=8, help_text=_('Server CAP'))
    degree = models.CharField(_('degree'), max_length=8, help_text=_('Server degree'))
    mastery = models.CharField(_('mastery'), max_length=8, help_text=_('Server mastery'))
    exp_rate = models.CharField(_('exp rate'), max_length=8, help_text=_('Server EXP rate'))
    exp_party_rate = models.CharField(_('exp party rate'), max_length=8, help_text=_('Server EXP party rate'))
    gold_drop_rate = models.CharField(_('gold drop rate'), max_length=8, help_text=_('Server gold drop rate'))
    item_drop_rate = models.CharField(_('item drop rate'), max_length=8, help_text=_('Server item drop rate'))
    alchemy_rate = models.CharField(_('alchemy rate'), max_length=8, help_text=_('Server alchemy rate'))
    website_link = models.URLField(_('website link'), blank=True, help_text=_('Server website'))
    website_register_link = models.URLField(_('website register link'), blank=True, help_text=_('Server website register link'))

    class Meta:
        verbose_name = _('Server')
        verbose_name_plural = _('Servers')

    def __unicode__(self):
        return u'Server %s' % (self.name.lower())

class ServerImage(models.Model):
    '''
    '''
    server = models.ForeignKey(Server)

    image = models.ImageField(upload_to='/server/')

    class Meta:
        verbose_name = _('Server image')
        verbose_name_plural = _('Server images')

    def __unicode__(self):
        return u'Image from server %s' % (self.server.name.lower())

class Video(models.Model):
    '''
    '''
    url = models.CharField(_('url'), max_length=64, help_text=_('Youtube video CODE (Ex: j4aGt6dUVj0 for http://www.youtube.com/watch?v=j4aGt6dUVj0)'))
    server = models.ForeignKey(Server)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def __unicode__(self):
        return u' '

class News(models.Model):
    '''
    '''
    title = models.CharField(_('title'), max_length=64, help_text=_('News title'))
    body = models.TextField(_('body'), max_length=512, help_text=_('News body'))
    server = models.ForeignKey(Server, verbose_name=_('Server'), help_text=_('Server'))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __unicode__(self):
        return u'New %s' % (self.name.lower())

class Type(models.Model):
    '''
    '''
    name = models.CharField(_('Name'), max_length=32, help_text=_('Type name'))

    class Meta:
        verbose_name = _('Type of price table')
        verbose_name_plural = _('Types of price tables')

    def __unicode__(self):
        return u'%s' % (self.name.upper())

class PriceTable(models.Model):
    '''
    '''
    type = models.ForeignKey(Type, verbose_name=_('Type'), help_text=_('Price table type'))
    server = models.ForeignKey(Server, verbose_name=_('Server'), help_text=_('Server'))

    class Meta:
        unique_together = ('type', 'server')
        verbose_name = _('Price table')
        verbose_name_plural = _('Price tables')

    def __unicode__(self):
        return u'Price table of server %s with type %s' % (self.type.name.lower(), self.server.name.lower())

class Price(models.Model):
    '''
    '''
    discrimination = models.CharField(_('Discrimination'), max_length=64, help_text=_('Discrimination of price'))
    real = models.DecimalField(_('Real'), max_digits=8, decimal_places=2, help_text=_('Real value (R$)'))
    bcash = models.DecimalField(_('BCash'), max_digits=8, decimal_places=2, help_text=_('BCash value (R$)'))
    pagseguro = models.DecimalField(_('PagSeguro'), max_digits=8, decimal_places=2, help_text=_('PagSeguro value (R$)'))
    paypal_real = models.DecimalField(_('Paypal real'), max_digits=8, decimal_places=2, help_text=_('Paypal real value (R$)'))
    paypal_dollar = models.DecimalField(_('Paypal dollar'), max_digits=8, decimal_places=2, help_text=_('Paypal dollar value'))
    price_table = models.ForeignKey(PriceTable, verbose_name=_('Price table'), help_text=_('Price table'))

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')

    def __unicode__(self):
        return u'Price table of server %s with type %s' % (self.type.name.lower(), self.server.name.lower())