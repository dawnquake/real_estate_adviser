from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Postcode

@admin.register(Postcode)
class PostcodeAdmin(admin.ModelAdmin):
    list_display = ('postcode',)  # Replace with actual field names