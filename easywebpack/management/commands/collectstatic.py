# -*- coding: utf-8
from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as CollectStaticCommand
from django.conf import settings

from ....webpack import webpack_build


class Command(CollectStaticCommand):
    def handle(self, *args, **kwargs):
        # Build webpack first
        self.stdout.write('Building Webpack...')
        if settings.DEBUG:
            webpack_build('production')
        else:
            webpack_build()

        # Continue with collectstatic
        super().handle(*args, **kwargs)
