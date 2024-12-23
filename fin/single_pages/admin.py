from django.contrib import admin
from .models import Portfolio, TeamMember

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'image')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'hook_text')