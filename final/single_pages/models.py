from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Raspberry(models.Model):
    CATEGORY_CHOICES = [
        ('sensor', 'Sensor'),
        ('input', 'Input'),
        ('control', 'Control'),
        ('output', 'Output'),
        ('etc', 'etc'),
    ]
    title = models.CharField(max_length=200)
    hook_text = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='raspberry/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    project_url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="프로젝트 URL"
    )

    def __str__(self):
        return self.title


class Ara(models.Model):
    CATEGORY_CHOICES = [
        ('led', 'Led'),
        ('oled', 'Oled'),
    ]
    title = models.CharField(max_length=200)
    hook_text = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='ara/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    project_url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="프로젝트 URL"
    )

    def __str__(self):
        return self.title


class Warning(models.Model):
    title = models.CharField(max_length=100)
    hook_text = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='warning/')

    def __str__(self):
        return f"{self.title}"