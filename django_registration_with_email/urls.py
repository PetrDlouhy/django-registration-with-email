from django.conf.urls import include
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import path, reverse_lazy
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView, ResendActivationView

from .forms import LoginForm, REPasswordResetForm, FullUserRegistrationForm
from .views import NextURLActivationView

urlpatterns = [
    # The first url is here only because othewise they get overriden by the activation key url
    path(
        'activate/complete/',
        TemplateView.as_view(
            template_name='registration/activation_complete.html',
        ),
        name='registration_activation_complete',
    ),
    path(
        'activate/resend/',
        ResendActivationView.as_view(),
        name='registration_resend_activation',
    ),
    path(
        'accounts/register/',
        RegistrationView.as_view(
            form_class=FullUserRegistrationForm,
        ),
        name='registration_register',
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
        'password_reset/',
        PasswordResetView.as_view(
            success_url=reverse_lazy('password_reset_done'),
            form_class=REPasswordResetForm,
            template_name='registration/password_reset_form.html',
        ),
        name='auth_password_reset',
    ),
    path('captcha/', include('captcha.urls')),
]
