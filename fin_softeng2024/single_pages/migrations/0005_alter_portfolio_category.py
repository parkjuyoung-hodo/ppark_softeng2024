# Generated by Django 4.1 on 2024-12-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("single_pages", "0004_alter_testimonial_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="category",
            field=models.CharField(max_length=50),
        ),
    ]
