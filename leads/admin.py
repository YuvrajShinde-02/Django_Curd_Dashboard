from django.contrib import admin
from .models import Lead
# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "source", "created_at")
    search_fields = ("name", "email", "source")
    list_filter = ("source", "created_at")