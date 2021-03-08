=====
Usage
=====

To use Django registration with email in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_registration_with_email.apps.DjangoRegistrationEmailConfig',
        ...
    )

Add Django registration with email's URL patterns:

.. code-block:: python

    from django_registration_with_email import urls as django_registration_with_email_urls


    urlpatterns = [
        ...
        url(r'^', include(django_registration_with_email_urls)),
        ...
    ]
