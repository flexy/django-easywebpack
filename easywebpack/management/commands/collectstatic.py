# -*- coding: utf-8
from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as CollectStaticCommand
from django.conf import settings

from easywebpack.webpack import webpack_build


class Command(CollectStaticCommand):
    def handle(self, *args, **kwargs):
        self.build_webpack()
        super(Command, self).handle(*args, **kwargs)

    def build_webpack(self):
        # Build webpack first
        self.stdout.write('Building Webpack...')
        if not settings.DEBUG:
            webpack_build('production')
        else:
            webpack_build()
