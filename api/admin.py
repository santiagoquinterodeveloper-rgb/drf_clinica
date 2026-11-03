from django.contrib import admin
from .models import Person
# Register your models here.

@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display= ['name', 'city', 'age']
