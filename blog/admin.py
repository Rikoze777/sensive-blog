from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdminPanel(admin.ModelAdmin):
    list_display = ['author', 'text', 'post']
    raw_id_fields = ['author']


@admin.register(Post)
class PostAdminPanel(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']


admin.site.register(Tag)
