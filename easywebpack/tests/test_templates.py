# -*- coding: utf-8 -*-
import pytest  # noqa

from django.template import Context, Template

"""
def create_template(filename):
    return '{{% load webpack_extras %}} {{% webpack_include "{0}" %}}'.format(filename)


def create_script_tag(filename):
    return '<script src="/static/webpack_build/{}"></script>'.format(filename)


def create_css_link_tag(filename):
    return '<link rel="stylesheet" type="text/css" href="/static/webpack_build/{}">'.format(filename)


def render_template(template):
    # render the template and trim whitespace
    # Something adds whitespace and I'm not sure what so I'm stripping it here
    return Template(template).render(Context()).strip()


def test_webpack_include_template_when_input_is_a_javascript_file(mocker):
    mocker.patch(
        'easywebpack.templatetags.webpack_extras.settings',
        django_settings_mock
    )

    input = 'fileA.js'
    expected = create_script_tag('fileA.1.js')
    template = create_template(input)
    actual = render_template(template)
    assert expected == actual

    input = 'fileB.js'
    expected = create_script_tag('fileB.2.js')
    template = create_template(input)
    actual = render_template(template)
    assert expected == actual


def test_webpack_include_template_when_input_is_a_css_file(mocker):
    mocker.patch('easywebpack.templatetags.webpack_extras.settings', django_settings_mock)

    input = 'styleB.css'
    expected = create_css_link_tag('styleB.2.css')
    template = create_template(input)
    actual = render_template(template)
    assert expected == actual

    input = 'styleC.css'
    expected = create_css_link_tag('styleC.3.css')
    template = create_template(input)
    actual = render_template(template)
    assert expected == actual
"""
