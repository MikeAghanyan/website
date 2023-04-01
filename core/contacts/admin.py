from django.contrib import admin

# Register your models here.
from .models import Contacts
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name', 'email']
    search_fields = ['id', 'name', 'email']