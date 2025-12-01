from django.contrib import admin
from .models import ContactRequest

# Register your models here.

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "created_at", "handled")
    list_filter = ("handled", "created_at")
    search_fields = ("full_name", "email", "company", "subject", "message")
