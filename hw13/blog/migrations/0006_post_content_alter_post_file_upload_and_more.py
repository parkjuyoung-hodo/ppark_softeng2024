# Generated by Django 5.1.2 on 2024-12-02 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_post_hook_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="file_upload",
            field=models.FileField(
                blank=True, null=True, upload_to="blog/images/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="head_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="blog/images/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=80)),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
        ),
    ]