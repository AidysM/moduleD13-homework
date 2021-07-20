from django.urls import path
from .views import ProfileView, replies_by_advert#, ReplyList
# from adverts.views import ReplyListView


urlpatterns = [
    path('', ProfileView.as_view()),
    path('<int:advert_pk>/', replies_by_advert, name='replies_by_advert'),
]
