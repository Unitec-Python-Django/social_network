from django.contrib.auth import get_user_model
from django.test import TestCase

from post.models import Post

UserModel = get_user_model()


class PostTestCase(TestCase):

    fixtures = [
        'users',
        'posts'
    ]

    def setUp(self) -> None:
        self.user = UserModel.objects.create(username='test')

    def test_check_created_at_after_post_creation(self):
        post = Post.objects.create(user=self.user, title='Test post')
        self.assertIsNotNone(post.created_at)

    def test_check_like_creation_after_like_toggle(self):
        post = Post.objects.create(user=self.user, title='Test post')
        post.toggle_like(self.user)
        self.assertEqual(post.count_likes, 1)
        self.assertEqual(post.post_like_history.count(), 1)

    def test_check_like_deletion_after_like_toggle(self):
        post = Post.objects.create(user=self.user, title='Test post')
        post.toggle_like(self.user)
        post.toggle_like(self.user)
        self.assertEqual(post.count_likes, 0)
        self.assertEqual(post.post_like_history.count(), 2)
