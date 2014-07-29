#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from redactor.widgets import RedactorEditor

from .models import (
	Info,
)

class InfoAdminForm(forms.ModelForm):
    class Meta:
        model = Info
        widgets = {
            'confirm_payment': RedactorEditor(),
            'how_to_buy': RedactorEditor(),
        }
