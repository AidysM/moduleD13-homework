from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm
from adverts.models import Reply, Advert


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_announcers'] = not self.request.user.groups.filter(name='announcers').exists()
        context['adverts'] = Advert.objects.filter(announcer=self.request.user.id).order_by('adv_name')
        context['replies'] = Reply.objects.filter(user=self.request.user).order_by('-created_reply')
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'protect/profile.html'
    form_class = UserForm
    success_url = '/'

