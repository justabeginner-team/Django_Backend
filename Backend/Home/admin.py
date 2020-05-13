from django.contrib import admin
from .models import Destination


class DisplayFields(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'offer')


# Register your models here.
admin.site.register(Destination, DisplayFields)
