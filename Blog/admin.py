from django.contrib import admin
from .models import PostsModel


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ['title']
# Register your models here.


admin.site.register(PostsModel, PostsAdmin)
