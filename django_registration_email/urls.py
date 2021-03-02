from django.conf.urls import include
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import path
from django.urls import reverse_lazy
from django_registration.backends.activation.views import RegistrationView
from django_registration.forms import RegistrationFormUniqueEmail

from .forms import REPasswordResetForm, LoginForm
from .views import NextURLActivationView


urlpatterns = [
    path(
        'accounts/register/',
        RegistrationView.as_view(
            form_class=RegistrationFormUniqueEmail,
        ),
        name='django_registration_register',
    ),
    path(
        'activate/<str:activation_key>/',
        NextURLActivationView.as_view(),
        name='registration_activate',
    ),
    path(
        'login/',
        LoginView.as_view(
            form_class=LoginForm,
            template_name='registration/login.html',
        ),
        name='auth_login',
    ),
    path(
        'password/reset/',
        PasswordResetView.as_view(
            success_url=reverse_lazy('auth_password_reset_done'),
            form_class=REPasswordResetForm,
        ),
        name='auth_password_reset',
    ),
    path('captcha/', include('captcha.urls')),
]
