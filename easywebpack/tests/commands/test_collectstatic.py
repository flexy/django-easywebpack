import pytest  # noqa

from easywebpack.management.commands import collectstatic


def test_handle(mocker):
    # Mock and patch
    super_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.collectstatic.CollectStaticCommand.handle',  # noqa
        super_mock,
    )

    build_webpack_mock = mocker.Mock()

    # Setup
    command = collectstatic.Command()
    command.build_webpack = build_webpack_mock

    # Checks
    command.handle()
    assert build_webpack_mock.called
    assert super_mock.called


def test_build_webpack(mocker):
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
    command = collectstatic.Command()
    command.stdout = stdout_mock

    # Debug is False
    settings_mock.DEBUG = False
    command.build_webpack()
    stdout_mock.write.assert_called_with(
        'Building Webpack...',
    )
    webpack_build_mock.assert_called_with('production')

    # Debug is True
    settings_mock.DEBUG = True
    command.build_webpack()
    webpack_build_mock.assert_called_with()
