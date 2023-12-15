from django.contrib import admin
from .models import Room, Room_type
# Register your models here.

admin.site.register(Room_type)
admin.site.register(Room)