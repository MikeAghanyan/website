from django.contrib import admin
from .models import HomeMotivation, Project, Blog, Service
# Register your models here.
@admin.register(HomeMotivation, Project, Blog, Service)
class MainPage(admin.ModelAdmin):
    list_display = ['id', 'titel']
    list_display_links = ['id', 'titel']
    search_fields = ['id', 'titel']