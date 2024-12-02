# Generated by Django 5.1.2 on 2024-12-02 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blog.category",
            ),
        ),
    ]
