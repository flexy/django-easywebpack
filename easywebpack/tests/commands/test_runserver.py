import pytest  # noqa

from easywebpack.management.commands import runserver


def test_inner_run(mocker):
    # Mock and patch
    webpack_build_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.runserver.webpack_build',
        webpack_build_mock,
    )

    stdout_mock = mocker.Mock()

    settings_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.runserver.settings',
        settings_mock,
    )

    # Setup
    command = runserver.CommandMixin()
    command.stdout = stdout_mock

    # DEBUG is false, Should not be called
    settings_mock.DEBUG = False
    command.inner_run()
    assert not webpack_build_mock.called

    # Debug is true
    settings_mock.DEBUG = True
    command.inner_run()
    stdout_mock.write.assert_called_with(
        'Building Webpack...',
    )
    webpack_build_mock.assert_called_with('development')
