import django_filters
from django.contrib.auth import get_user_model
from django.db.models import Q

from post.models import Post

UserModel = get_user_model()


class PostFilter(django_filters.FilterSet):
    users = django_filters.ModelMultipleChoiceFilter(queryset=UserModel.objects.all(), field_name='user')
    posted_time = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')
    search = django_filters.CharFilter(method='search_filter')

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(description__icontains=value) | Q(title__icontains=value))

    class Meta:
        model = Post
        fields = ['users', 'posted_time', 'search']
