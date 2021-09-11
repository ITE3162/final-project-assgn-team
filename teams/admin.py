from django.contrib import admin

# Register your models here.
from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description')
    list_filter = ('name', 'title')
    search_fields = ('name', 'title')
