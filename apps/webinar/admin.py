from django.contrib import admin
from .models import Webinar


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ['id']
    filter_horizontal = ['tags']
