# -*- coding: utf-8 -*-
import json
from subprocess import call

from django.conf import settings


def load_webpack_manifest():
    manifest = str(settings.EASYWEBPACK['MANIFEST'])

    with open(manifest) as manifest_file:
        manifest_files = json.load(manifest_file)

    return manifest_files


def get_manifest_file_and_type(filename):
    manifest_files = load_webpack_manifest()

    file = manifest_files[filename]
    type = file.split('.')[-1]

    return {
        'file': file,
        'filetype': type
    }


def webpack_build(environment='development'):
    call([
        'webpack',
        '--env.{}'.format(environment),
        '--mode={}'.format(environment),
    ])
