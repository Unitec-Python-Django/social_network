import django_filters
from django.contrib.auth import get_user_model

from post.models import Post

UserModel = get_user_model()


class PostFilter(django_filters.FilterSet):
    users = django_filters.ModelMultipleChoiceFilter(queryset=UserModel.objects.all(), field_name='user')
    posted_time = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')

    class Meta:
        model = Post
        fields = ['users', 'posted_time']
