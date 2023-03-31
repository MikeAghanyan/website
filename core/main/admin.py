from django.contrib import admin
from .models import HomeMotivation, Project, Blog, Service, My
# Register your models here.
@admin.register(HomeMotivation, Project, Blog, Service, My)
class MainPage(admin.ModelAdmin):
    list_display = ['id', 'titel']
    list_display_links = ['id', 'titel']
    search_fields = ['id', 'titel']

# prepopulated_fields = {"slug": ("title",)} - Now head over to the admin and add a new article. 
# You'll note that as you type in the Title field, the Slug field is automatically populated. Pretty neat!