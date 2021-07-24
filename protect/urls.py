from django.urls import path
from .views import ProfileView, replies_by_advert#, ReplyList
# from protect.views import Replyiew
from adverts.views import ReplyDeleteView


urlpatterns = [
    path('', ProfileView.as_view()),
    path('<int:advert_pk>/', replies_by_advert, name='replies_by_advert'),
    path('<int:advert_pk>/delete/', ReplyDeleteView.as_view(), name='adv_reply_delete')

]
