from django.contrib.auth import mixins
from django.views import View


class LoginRequiredMixin(mixins.LoginRequiredMixin, View):
    pass
















