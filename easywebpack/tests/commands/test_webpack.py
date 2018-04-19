import pytest  # noqa

from easywebpack.management.commands import webpack


def test_add_arguments(mocker):
    # Mock and patch
    parser_mock = mocker.Mock()

    # Setup
    command = webpack.Command()

    # Check
    command.add_arguments(parser_mock)
    parser_mock.add_argument.assert_called_with(
        '--environment',
        dest='environment',
        help='Choose build environment',
    )


def test_handle(mocker):
    # Mock and patch
    webpack_build_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.management.commands.webpack.webpack_build',
        webpack_build_mock,
    )

    stdout_mock = mocker.Mock()

    # Setup
    command = webpack.Command()
    command.stdout = stdout_mock

    # Environment not provided
    command.handle()
    stdout_mock.write.assert_called_with(
        'Building Webpack...',
    )
    webpack_build_mock.assert_called_with()

    # Environment provided
    command.handle(
        environment='development',
    )
    webpack_build_mock.assert_called_with('development')
