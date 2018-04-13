from django.contrib.staticfiles.management.commands.runserver import \
    Command as StaticfilesRunserverCommand
from django.conf import settings

from ..webpack import webpack_build


class Command(StaticfilesRunserverCommand):
    def inner_run(self, *args, **kwargs):
        # Build webpack first if in DEBUG
        if settings.DEBUG:
            self.stdout.write('Building Webpack...')
            webpack_build('development')

        # Continue with runserver
        super().inner_run(*args, **kwargs)
