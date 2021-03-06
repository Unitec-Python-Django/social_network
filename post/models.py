from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(null=True, blank=True, max_length=25)
    photo = models.ImageField(upload_to='post', null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def count_likes(self):
        return self.post_likes.count()

    @property
    def count_comments(self):
        return self.post_comments.count()

    @transaction.atomic
    def toggle_like(self, user):
        if self.post_likes.filter(user=user).exists():
            self.post_likes.filter(user=user).delete()
            self.post_like_history.create(user=self.user, like=False)
        else:
            self.post_likes.create(user=user)
            self.post_like_history.create(user=self.user, like=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'user']


class PostLikeHistory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like_history')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_like_history')
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)
