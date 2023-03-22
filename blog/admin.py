from django.contrib import admin

from blog.models import Comment, Post

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'text', 'post_date')

    search_fields = ['title', 'text']
    date_hierarchy = 'post_date'
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'owner', 'text')

    list_per_page = 20
