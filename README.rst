==================
django-easywebpack
==================

Making Django and Webpack best friends.

.. image:: https://badge.fury.io/py/django-easywebpack.svg
    :target: https://badge.fury.io/py/django-easywebpack

.. image:: https://travis-ci.org/fndrz/django-easywebpack.svg?branch=master
    :target: https://travis-ci.org/fndrz/django-easywebpack

.. image:: https://codecov.io/gh/fndrz/django-easywebpack/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/fndrz/django-easywebpack

.. image:: https://readthedocs.org/projects/django-easywebpack/badge/?version=latest
    :target: http://django-easywebpack.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Documentation
-------------

The full documentation is at https://django-easywebpack.readthedocs.io.

Quickstart
----------

Install django-easywebpack::

    pip install django-easywebpack

Add it to your `INSTALLED_APPS`:

  Note: :code:`easywebpack` must be placed before :code:`staticfiles` for
  :code:`./manage.py` commands to work properly.

.. code-block:: python

    INSTALLED_APPS = (
        'easywebpack',
        ...
    )

Then, configure it in your Django settings:

.. code-block:: python

    EASYWEBPACK = {
        'MANIFEST': 'path/to/manifest.json',
    }

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
