============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/fndrz/django-easywebpack/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

django-easywebpack could always use more documentation, whether as part of the
official django-easywebpack docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/fndrz/django-easywebpack/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `django-easywebpack` for local development.

1. Fork the `django-easywebpack` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:<GitHub username>/django-easywebpack.git

3. Install requirements and create a development environment::

    $ pip install pipenv
    $ pipenv install --dev
    $ pipenv shell

4. Create a branch for local development::

    $ git checkout -b <bugfix/feature name>

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

        $ pytest --flake8
        $ pytest
        $ tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin <bugfix/feature name>

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, and 3.3, and for PyPy. Check
   https://travis-ci.org/fndrz/django-easywebpack/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ pytest <module>

Releasing
---------

First, run Punch to create a version update::

    $ punch --part <major|minor|patch>

Once everything has been merged into master, build the package::

    $ python setup.py sdist bdist_wheel

Then, verify it on TestPyPI::

    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Once everything looks good, upload the package to PyPI::

    $ twine upload dist/*
