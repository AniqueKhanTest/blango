from django.contrib import admin

from .models import Tag, Post, Comment, AuthorProfile

# Register your models here.
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["id",'slug', 'title',"author" , 'published_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)
