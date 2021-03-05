==============================
Django registration with email
==============================

.. image:: https://badge.fury.io/py/django-registration-with-email.svg
    :target: https://badge.fury.io/py/django-registration-with-email

.. image:: https://travis-ci.org/PetrDlouhy/django-registration-with-email.svg?branch=master
    :target: https://travis-ci.org/PetrDlouhy/django-registration-with-email

.. image:: https://codecov.io/gh/PetrDlouhy/django-registration-with-email/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/PetrDlouhy/django-registration-with-email

Override (django-registration)[https://github.com/ubernostrum/django-registration] to log-in by e-mail.
This package provides:

- Log-in with e-mail or username
- User-convenient messages for various cases in login and password reset form
- Send password reset e-mail even for users without password
- Includes phishing-safe next_url mechanism

Security note: For better user experience the password reset form informs users if the e-mail doesn't exist in the system.
This lowers security, because attacker can query the system whether the account exists or not. The risk is lowered by
using captcha on the form, but still you should evaluate if this is secure enough for your system.

Documentation
-------------

The full documentation is at https://django-registration-with-email.readthedocs.io.

Quickstart
----------

Install Django registration with email::

    pip install django-registration-with-email

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_registration',
        'django_registration_with_email',
        'captcha',
        ...
    )

Add Django registration with email's URL patterns:

.. code-block:: python


    urlpatterns = [
        ...
        url(r'^', include('django_registration_with_email.urls')),
        ...
    ]

Set email as unique=True in your User model:

.. code-block:: python

   class User(TimeStampedModel, AbstractUser):
      email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        blank=True,
        null=True,
        unique=True,
    )

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
