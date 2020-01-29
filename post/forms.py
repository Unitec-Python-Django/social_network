from django.forms import ModelForm

from post.models import Post


class PostUploadForm(ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'description')
