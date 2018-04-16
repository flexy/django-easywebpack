# -*- coding: utf-8 -*-
import pytest  # noqa
import os

from ..webpack import \
    load_webpack_manifest, \
    get_manifest_file_and_type


def test_load_webpack_manifest(mocker):
    # Mock and patch
    django_settings_mock = mocker.Mock()
    django_settings_mock.WEBPACK = {
        'MANIFEST': '{}/manifest.json'.format(
            os.path.dirname(os.path.abspath(__file__))
        ),
    }
    mocker.patch(
        'easywebpack.webpack.settings',
        django_settings_mock,
    )

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
    actual = load_webpack_manifest()
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
    actual = get_manifest_file_and_type(filename)
    assert expected == actual
