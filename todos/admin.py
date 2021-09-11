from django.contrib import admin
from todos.models import Activity


# Register your models here.
@admin.register(Activity)
class Activityadmin(admin.ModelAdmin):
    list_display = ('title','description')
    list_filter = ('title','description')