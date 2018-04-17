# -*- coding: utf-8
from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as CollectStaticCommand
from django.conf import settings

from easywebpack.webpack import webpack_build


class CommandMixin:
    def handle(self, *args, **kwargs):
        # Build webpack first
        self.stdout.write('Building Webpack...')
        if not settings.DEBUG:
            webpack_build('production')
        else:
            webpack_build()


class Command(CommandMixin, CollectStaticCommand):
    pass
