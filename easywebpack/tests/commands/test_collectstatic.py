import pytest  # noqa

from easywebpack.management.commands import collectstatic


def test_handle(mocker):
    # Mock and patch
    webpack_build_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.collectstatic.webpack_build',
        webpack_build_mock,
    )

    stdout_mock = mocker.Mock()

    settings_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.collectstatic.settings',
        settings_mock,
    )

    # Setup
    command = collectstatic.CommandMixin()
    command.stdout = stdout_mock

    # Debug is False
    settings_mock.DEBUG = False
    command.handle()
    stdout_mock.write.assert_called_with(
        'Building Webpack...',
    )
    webpack_build_mock.assert_called_with('production')

    # Debug is True
    settings_mock.DEBUG = True
    command.handle()
    webpack_build_mock.assert_called_with()
