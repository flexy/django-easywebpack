=====
Setup
=====

Installation
------------

At the command line::

    $ pip install django-easywebpack

Configuration
-------------

Webpack
~~~~~~~

django-easywebpack requires the `webpack-manifest-plugin
<https://github.com/danethurber/webpack-manifest-plugin>`_.

To configure it, install webpack-manifest-plugin with yarn or npm::

    $ yarn add webpack-manifest-plugin

Add webpack-manifest-plugin into :code:`webpack.config.js`:

.. code-block:: javascript
    :emphasize-lines: 1, 8

    var ManifestPlugin = require('webpack-manifest-plugin');

    const config = {

      ...

      plugins: [
        new ManifestPlugin()
      ]

      ...

    }

Django
~~~~~~

To use django-easywebpack, add it to your `INSTALLED_APPS`:

  Note: :code:`'easywebpack'` must be placed before the staticfiles app
  for the management commands to work properly.

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
