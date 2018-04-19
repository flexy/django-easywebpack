# -*- coding: utf-8
from django.contrib.staticfiles.management.commands.runserver import \
    Command as StaticfilesRunserverCommand
from django.conf import settings

from easywebpack.webpack import webpack_build


class Command(StaticfilesRunserverCommand):
    def inner_run(self, *args, **kwargs):
        self.build_webpack()
        super(Command, self).inner_run(*args, **kwargs)

    def build_webpack(self):
        # Build webpack first if in DEBUG
        if settings.DEBUG:
            self.stdout.write('Building Webpack...')
            webpack_build('development')
