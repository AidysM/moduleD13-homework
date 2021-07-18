from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    announcers_group = Group.objects.get(name='announcers')
    if not request.user.groups.filter(name='announcers').exists():
        announcers_group.user_set.add(user)
    return redirect('/')

