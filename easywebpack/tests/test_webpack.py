# -*- coding: utf-8 -*-
import pytest  # noqa

from .. import webpack


def test_load_webpack_manifest(mocker):
    # Determine expected values
    expected = {
        'fileA.js': 'fileA.1.js',
        'fileB.js': 'fileB.2.js',
        'fileC.js': 'fileC.3.js',
        'styleA.css': 'styleA.1.css',
        'styleB.css': 'styleB.2.css',
        'styleC.css': 'styleC.3.css'
    }

    # Verify results
    actual = webpack.load_webpack_manifest()
    assert expected == actual


def test_get_manifest_file_and_type(mocker):
    # Mock and patch
    load_webpack_manifest_mock = mocker.Mock()
    load_webpack_manifest_mock.return_value = {
        'test.js': 'test.1.js',
    }
    mocker.patch(
        'easywebpack.webpack.load_webpack_manifest',
        load_webpack_manifest_mock
    )

    filename = 'test.js'

    # Determine expected values
    expected = {
        'file': 'test.1.js',
        'filetype': 'js',
    }

    # Verify results
    actual = webpack.get_manifest_file_and_type(filename)
    assert expected == actual


def test_webpack_build(mocker):
    # Mock and patch
    call_mock = mocker.Mock()
    mocker.patch(
        'easywebpack.webpack.call',
        call_mock,
    )

    # Determine expected values
    expected_arguments = [
        'webpack',
        '--env.development',
        '--mode=development',
    ]

    expected_arguments_production = [
        'webpack',
        '--env.production',
        '--mode=production',
    ]

    # Verify results
    webpack.webpack_build()
    call_mock.assert_called_with(expected_arguments)

    # Environment specified
    webpack.webpack_build('production')
    call_mock.assert_called_with(expected_arguments_production)
