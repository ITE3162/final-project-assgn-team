from django.contrib import admin

# Register your models here.
from about.models import AboutUs


@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = ('heading', 'description', 'logo')
