from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_announcers'] = not self.request.user.groups.filter(name='announcers').exists()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'protect/profile.html'
    form_class = UserForm
    success_url = '/'

