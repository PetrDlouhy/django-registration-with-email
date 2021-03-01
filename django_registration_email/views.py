from next_url_mixin.mixin import NextUrlMixin
from registration.backends.default.views import ActivationView


class NextURLActivationView(NextUrlMixin, ActivationView):
    pass
