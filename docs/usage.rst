=====
Usage
=====

Template tags
-------------

The provided template tags must be loaded before they can be used:

.. code-block:: html

    {% load webpack_extras %}

``webpack_include``
~~~~~~~~~~~~~~~~~~~

:code:`{% webpack_include filename %}`

Includes a file from the Webpack manifest. Only JS and CSS files are
currently supported.

Example:
````````

.. code-block:: html

    {% load webpack_extras app.js %}


Management commands
-------------------

``runserver``
~~~~~~~~~~~~~

:code:`$ django-admin runserver`

If :code:`settings.DEBUG` is :code:`True`, this runs webpack with
:code:`--env.development --mode=development`.

``collectstatic``
~~~~~~~~~~~~~~~~~

:code:`$ django-admin collectstatic`

If :code:`settings.DEBUG` is :code:`True`, this runs webpack with
:code:`--env.development --mode=development`.

Otherwise, it runs webpack with :code:`--env.production --mode=production`.

``webpack``
~~~~~~~~~~~

:code:`$ django-admin webpack`

This command runs webpack. By default, it uses a :code:`development`
environment.

Options:

:code:`--environment`

  Selects a build environment. It can be set to ``production`` or
  ``development``.
