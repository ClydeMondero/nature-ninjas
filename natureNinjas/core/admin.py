from django.contrib import admin
from .models import Article, Multimedia, Activity


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'activity', 'multimedia')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_url', 'created_at')
    list_filter = ('created_at',)
