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
