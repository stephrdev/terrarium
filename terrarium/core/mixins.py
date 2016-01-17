from django.contrib.auth.views import REDIRECT_FIELD_NAME, login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from .forms import LoginForm


class LoginRequiredMixin(object):

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            login_defaults = {
                'authentication_form': LoginForm,
                'template_name': 'login.html',
                'extra_context': {
                    'next_field': REDIRECT_FIELD_NAME,
                    'next_value': request.get_full_path(),
                },
            }
            return login(request, **login_defaults)

        return super().dispatch(request, *args, **kwargs)
