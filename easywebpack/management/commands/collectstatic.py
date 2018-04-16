# -*- coding: utf-8
from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as CollectStaticCommand

from ....webpack import webpack_build


class Command(CollectStaticCommand):
    def handle(self, *args, **kwargs):
        # Build webpack first
        self.stdout.write('Building Webpack...')
        webpack_build('production')

        # Continue with collectstatic
        super().handle(*args, **kwargs)
