from subprocess import call


def webpack_build(environment='development'):
    call([
        'webpack',
        f'--env.{environment}',
        f'--mode={environment}',
    ])
