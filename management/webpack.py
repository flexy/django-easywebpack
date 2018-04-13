from subprocess import call


def webpack_build():
    call(['yarn', 'run', 'build'])
