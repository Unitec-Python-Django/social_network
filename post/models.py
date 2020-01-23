from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField()
    description = models.TextField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
