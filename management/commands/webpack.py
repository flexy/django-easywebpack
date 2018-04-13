from django.core.management.base import BaseCommand

from ..webpack import webpack_build


class Command(BaseCommand):
    help = 'Builds webpack'

    def handle(self, *args, **kwargs):
        self.stdout.write('Building Webpack...')
        webpack_build()
