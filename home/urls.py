from django.urls import path

from home.views import HomeIndex, PostIndexView, PostDetailView, PostDetailTypeView, UploadIndexView, ChatIndexView, \
    ChatDetailView, LoginIndexView

urlpatterns = [
    path('login/', LoginIndexView.as_view(), name='login'),
    path('home/', HomeIndex.as_view(), name='home'),
    path('upload/', UploadIndexView.as_view(), name='upload'),
    path('chat/', ChatIndexView.as_view(), name='chat'),
    path('chat/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('posts/', PostIndexView.as_view(), name='posts_index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts_detail'),
    path('posts/<int:pk>/types/<str:type>/', PostDetailTypeView.as_view(), name='posts_detail_type'),

]
