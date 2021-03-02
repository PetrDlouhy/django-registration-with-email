from django_registration.backends.activation.views import ActivationView
from next_url_mixin.mixin import NextUrlMixin


class NextURLActivationView(NextUrlMixin, ActivationView):
    pass
