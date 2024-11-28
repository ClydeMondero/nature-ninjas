from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=200)  # Title of the article
    content = models.TextField()  # Main content of the article
    image = models.ImageField(upload_to="articles/")  # Featured image
    slug = models.SlugField(unique=True, blank=True)  # SEO-friendly URL
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the article was created

    # New relationships
    activity = models.ForeignKey(
        'Activity', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles'
    )
    multimedia = models.ForeignKey(
        'Multimedia', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles'
    )

    def save(self, *args, **kwargs):
        # Automatically generate slug from title if not set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Multimedia(models.Model):
    title = models.CharField(max_length=200)  # Title of the multimedia content
    description = models.TextField(blank=True)  # Description of the multimedia content
    file = models.FileField(upload_to="multimedia/")  # File upload (e.g., video, audio, or infographic)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title

from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='activities/', blank=True, null=True)
    external_url = models.URLField(blank=True, null=True)
    preview_image = models.ImageField(upload_to='activity_previews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title
