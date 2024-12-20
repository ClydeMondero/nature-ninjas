# Generated by Django 5.1.3 on 2024-11-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='articles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
