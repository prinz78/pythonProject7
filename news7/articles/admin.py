from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentStackedInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentStackedInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)