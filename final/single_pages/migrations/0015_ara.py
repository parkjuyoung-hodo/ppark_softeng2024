# Generated by Django 4.1 on 2024-12-23 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("single_pages", "0014_alter_raspberry_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ara",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[("led", "Led"), ("oled", "Oled")], max_length=50
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="ara/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "project_url",
                    models.URLField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="프로젝트 URL",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
