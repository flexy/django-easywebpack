import pytest  # noqa

from easywebpack.management.commands import runserver


def test_inner_run(mocker):
    # Mock and patch
    super_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.runserver.StaticfilesRunserverCommand.inner_run',  # noqa
        super_mock,
    )

    build_webpack_mock = mocker.Mock()

    # Setup
    command = runserver.Command()
    command.build_webpack = build_webpack_mock

    # Checks
    command.inner_run()
    assert build_webpack_mock.called
    assert super_mock.called


def test_build_webpack(mocker):
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
    command = runserver.Command()
    command.stdout = stdout_mock

    # DEBUG is false, Should not be called
    settings_mock.DEBUG = False
    command.build_webpack()
    assert not webpack_build_mock.called

    # Debug is true
    settings_mock.DEBUG = True
    command.build_webpack()
    stdout_mock.write.assert_called_with(
        'Building Webpack...',
    )
    webpack_build_mock.assert_called_with('development')
