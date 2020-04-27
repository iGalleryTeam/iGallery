# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth_'

    def ready(self):
        import auth_.signals
