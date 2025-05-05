from django.contrib import admin
from .models import FoodEntry

@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'calories', 'date_consumed')
    list_filter = ('date_consumed',)
    search_fields = ('food_name',)
