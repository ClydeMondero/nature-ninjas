# Generated by Django 5.1.3 on 2024-11-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_activity_external_url_alter_activity_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='activity_previews/'),
        ),
    ]
