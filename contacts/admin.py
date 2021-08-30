from django.contrib import admin
from .models import ContactInfo


# Register your models here.

@admin.register(ContactInfo)
class ContactInfo(admin.ModelAdmin):
    list_display = ('sender', 'subject', 'contacted_date')
    list_filter = ('sender', 'contacted_date')
    search_fields = ('sender', 'subject')
