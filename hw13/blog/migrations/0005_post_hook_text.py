# Generated by Django 5.1.2 on 2024-12-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]