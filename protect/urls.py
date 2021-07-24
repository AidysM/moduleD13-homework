from django.urls import path
from .views import ProfileView, replies_by_advert

from .views import take_reply


urlpatterns = [
    path('', ProfileView.as_view()),
    path('<int:advert_pk>/', replies_by_advert, name='replies_by_advert'),
    path('<int:advert_pk>/take_reply/', take_reply, name='reply_take')
    # path('<int:advert_pk>/delete/', ReplyDeleteView.as_view(), name='adv_reply_delete')

]
