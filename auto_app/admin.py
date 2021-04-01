from django.contrib import admin
from auto_app.models import Car
# Register your models here.

@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
	pass