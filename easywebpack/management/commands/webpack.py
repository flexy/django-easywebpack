# -*- coding: utf-8
from django.core.management.base import BaseCommand

from ....webpack import webpack_build


class Command(BaseCommand):
    help = 'Builds webpack'

    def add_arguments(self, parser):
        parser.add_argument(
            '--environment',
            dest='environment',
            help='Choose build environment',
        )

    def handle(self, *args, **kwargs):
        self.stdout.write('Building Webpack...')

        if kwargs['environment']:
            webpack_build(kwargs['environment'])
        else:
            webpack_build()
