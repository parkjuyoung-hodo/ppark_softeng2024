from django.contrib import admin
from .models import Raspberry, Warning, Ara

@admin.register(Raspberry)
class RaspberryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'image')

@admin.register(Ara)
class AraAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'image')

@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('title', 'hook_text')