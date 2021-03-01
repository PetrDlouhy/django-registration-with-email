=====
Usage
=====

To use Django registration email in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_registration_email.apps.DjangoRegistrationEmailConfig',
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
