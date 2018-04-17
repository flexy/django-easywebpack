# -*- coding: utf-8
from django.core.management.base import BaseCommand

from easywebpack.webpack import webpack_build


class CommandMixin:
    def add_arguments(self, parser):
        parser.add_argument(
            '--environment',
            dest='environment',
            help='Choose build environment',
        )

    def handle(self, *args, **kwargs):
        self.stdout.write('Building Webpack...')

        if 'environment' in kwargs:
            webpack_build(kwargs['environment'])
        else:
            webpack_build()


class Command(CommandMixin, BaseCommand):
    help = 'Builds webpack'
