from django.conf.urls import url
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from registration.backends.default.views import ResendActivationView

from .forms import REPasswordResetForm, LoginForm
from .views import NextURLActivationView


urlpatterns = [
    # The first two urls are here only because othewise they get overriden by the activation key url
    url(
        r'^activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete',
    ),
    url(
        r'^activate/resend/$',
        ResendActivationView.as_view(),
        name='registration_resend_activation',
    ),
    url(
        r'^activate/(?P<activation_key>\w+)/$',
        NextURLActivationView.as_view(),
        name='registration_activate',
    ),
    url(
        r'^login/?$',
        LoginView.as_view(
            form_class=LoginForm,
            template_name='registration/login.html',
        ),
        name='auth_login',
    ),
    url(
        r'^password/reset/$',
        PasswordResetView.as_view(
            success_url=reverse_lazy('auth_password_reset_done'),
            form_class=REPasswordResetForm,
        ),
        name='auth_password_reset',
    ),
]
