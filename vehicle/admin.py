from django.contrib import admin

from vehicle.models import Car


@admin.register(Car)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
