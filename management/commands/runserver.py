from django.contrib.staticfiles.management.commands.runserver import \
    Command as StaticfilesRunserverCommand

from ..webpack import webpack_build


class Command(StaticfilesRunserverCommand):
    def inner_run(self, *args, **kwargs):
        # Build webpack first
        self.stdout.write('Building Webpack...')
        webpack_build()

        # Continue with runserver
        super().inner_run(*args, **kwargs)
