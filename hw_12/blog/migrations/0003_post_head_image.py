# Generated by Django 5.1.2 on 2024-11-30 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_updated_at_alter_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="head_image",
            field=models.ImageField(blank=True, upload_to="blog/images/%Y/%m/%d/"),
        ),
    ]