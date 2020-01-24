from django.contrib import admin

from post.models import Post, PostLike, PostLikeHistory, PostComment

admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(PostLikeHistory)
admin.site.register(PostComment)
