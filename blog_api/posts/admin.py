from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'title',
        'text',
        'created',
        'updated',
    )
    list_display_links = (
        'pk',
        'title',
    )
    list_filter = ('created',)


admin.site.register(Post, PostAdmin)
