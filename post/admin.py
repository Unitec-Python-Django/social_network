from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from post.models import Post, PostLike, PostLikeHistory, PostComment


class PostAdmin(TranslationAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostLike)
admin.site.register(PostLikeHistory)
admin.site.register(PostComment)
