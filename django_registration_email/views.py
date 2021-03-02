from next_url_mixin.mixin import NextUrlMixin
from django_registration.backends.activation.views import ActivationView


class NextURLActivationView(NextUrlMixin, ActivationView):
    pass
