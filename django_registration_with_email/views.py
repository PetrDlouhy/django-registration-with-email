from registration.backends.default.views import ActivationView
from next_url_mixin.mixin import NextUrlMixin


class NextURLActivationView(NextUrlMixin, ActivationView):
    pass
