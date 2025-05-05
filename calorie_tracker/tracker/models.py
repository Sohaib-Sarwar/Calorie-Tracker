from django.db import models
from django.urls import reverse

class FoodEntry(models.Model):
    food_name = models.CharField(max_length=200)
    calories = models.IntegerField()
    date_consumed = models.DateField()
    
    def __str__(self):
        return f"{self.food_name} - {self.calories} calories on {self.date_consumed}"
    
    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_consumed', 'food_name']
        verbose_name_plural = 'Food Entries'
