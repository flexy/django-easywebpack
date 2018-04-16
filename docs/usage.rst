=====
Usage
=====

To use django-easywebpack in a project, add it to your `INSTALLED_APPS`:

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

In your templates
-----------------

First, load the :code:`easywebpack` tags:

.. code-block:: html

    {% load webpack_extras %}

You can then include files from your :code:`webpack.config`:

    Only JS and CSS files are currently supported

.. code-block:: html

    {% webpack_include filename %}


Management commands
-------------------

``runserver``
~~~~~~~~~~~~~

:code:`django-admin runserver`

If :code:`settings.DEBUG` is :code:`True`, this runs webpack with
:code:`--env.development --mode=development`.

``collectstatic``
~~~~~~~~~~~~~~~~~

:code:`django-admin collectstatic`

If :code:`settings.DEBUG` is :code:`True`, this runs webpack with
:code:`--env.development --mode=development`.

Otherwise, it runs webpack with :code:`--env.production --mode=production`.

``webpack``
~~~~~~~~~~~

:code:`django-admin webpack`

This command runs webpack. By default, it uses a :code:`development`
environment.

Options:

:code:`--environment`

  Selects a build environment. It can be set to ``production`` or
  ``development``.
