__config_version__ = 1

GLOBALS = {
    'serializer': '{{major}}.{{minor}}.{{patch}}',
}

FILES = [
    'setup.py',
    'easywebpack/__init__.py',
]

VERSION = ['major', 'minor', 'patch']

VCS = {
    'name': 'git',
    'options': {
        'make_release_branch': False,
    }
}
