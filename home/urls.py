from django.urls import path

from home.views import HomeIndex, PostIndexView, PostDetailView, PostDetailTypeView

urlpatterns = [
    path('home/', HomeIndex.as_view(), name='home'),
    path('posts/', PostIndexView.as_view(), name='posts_index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts_detail'),
    path('posts/<int:pk>/types/<str:type>/', PostDetailTypeView.as_view(), name='posts_detail_type'),

]
