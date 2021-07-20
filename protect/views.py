import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .forms import UserForm
from adverts.models import Reply, Advert


def replies_by_advert(request, advert_pk):
    # for advert in adverts:
    adv_replies = Reply.objects.filter(advert=advert_pk).order_by('created_reply')
    context = {'adv_replies': adv_replies}
    return render(request, 'protect/replies.html', context)


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


# class ReplyList(ListView):
#     model = Reply
#     template_name = 'protect/replies.html'
#     # context_object_name = 'replies'
#     queryset = Reply.objects.order_by('-created_reply')
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         replies = Advert.replies.all()
#         context['replies'] = replies
#
#         return context
