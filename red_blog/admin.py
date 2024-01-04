from django.contrib import admin

from .models import PostFile


@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ["title", "code", "download_count"]
    search_field = ["title", ]
    exclude = ["download_count", ]
