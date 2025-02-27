from django.contrib import admin
from .models import Post, Tag

admin.site.register(Post)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tag,TagAdmin)

# Register your models here.