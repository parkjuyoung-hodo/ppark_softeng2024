from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('product', 'Product'),
        ('branding', 'Branding'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
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