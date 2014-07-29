#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from gastroprocto.apps.gui.generic_view import GenericView
from gastroprocto.apps.core.models import (
    Server,
    Banner,
)

class GUIView(GenericView):
    def home(self, request):
        data = None

        page_title = 'Home | gastroprocto'
        banners = Banner.objects.filter(active=True).order_by('-date')[:5]

        data = {
            'template': {
                'page_title' : page_title,
                'banners' : banners,
            }
        }

        return data

class ServerView(GenericView):
    def privates(self, request):
        data = None

        servers = Server.objects.filter(originality="private")

        data = {
            'template' : {
                'servers' : servers,
            }
        }
        return data
