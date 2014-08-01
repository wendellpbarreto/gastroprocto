#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from gastroprocto.apps.gui.generic_view import GenericView

class GUIView(GenericView):
    def home(self, request):
        data = None

        page_title = 'Home | gastroprocto'

        data = {
            'template': {
                'page_title' : page_title,
            }
        }

        return data
