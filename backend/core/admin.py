# Register your models here.
from django.contrib import admin
from .models import Contact


# register the instance to the db
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "email")
