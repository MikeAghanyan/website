from django.contrib import admin
from .models import HomeMotivation, Project, Blog, Services, My, ServicesAll
# Register your models here.
@admin.register(HomeMotivation, Project, Blog, Services, My)
class ServicesAllPage(admin.ModelAdmin):
    list_display = ['id', 'titel']
    list_display_links = ['id', 'titel']
    search_fields = ['id', 'titel']

@admin.register( ServicesAll)
class DetailsPage(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']

# prepopulated_fields = {"slug": ("title",)} - Now head over to the admin and add a new article. 
# You'll note that as you type in the Title field, the Slug field is automatically populated. Pretty neat!