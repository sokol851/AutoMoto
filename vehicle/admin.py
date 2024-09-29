from django.contrib import admin

from vehicle.models import Car, Moto, Milage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)


@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)


@admin.register(Milage)
class MilageAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'moto', 'milage', 'year',)
