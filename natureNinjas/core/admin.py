from django.contrib import admin
from .models import Article, Multimedia, Activity, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'activity', 'multimedia', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category',)


@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_url', 'created_at')
    list_filter = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}