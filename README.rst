=============================
Django registration email
=============================

.. image:: https://badge.fury.io/py/django-registration-email.svg
    :target: https://badge.fury.io/py/django-registration-email

.. image:: https://travis-ci.org/PetrDlouhy/django-registration-email.svg?branch=master
    :target: https://travis-ci.org/PetrDlouhy/django-registration-email

.. image:: https://codecov.io/gh/PetrDlouhy/django-registration-email/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/PetrDlouhy/django-registration-email

Override (django-registration)[https://github.com/ubernostrum/django-registration] to log in by e-mail

Documentation
-------------

The full documentation is at https://django-registration-email.readthedocs.io.

Quickstart
----------

Install Django registration email::

    pip install django-registration-email

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_registration_email',
        ...
    )

Add Django registration email's URL patterns:

.. code-block:: python

    from django_registration_email import urls as django_registration_email_urls


    urlpatterns = [
        ...
        url(r'^', include(django_registration_email_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
