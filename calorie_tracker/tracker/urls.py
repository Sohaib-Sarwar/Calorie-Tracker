from django.urls import path
from .views import (
    HomeView,
    FoodEntryListView,
    FoodEntryDetailView,
    FoodEntryCreateView,
    FoodEntryUpdateView,
    FoodEntryDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('entries/', FoodEntryListView.as_view(), name='entry-list'),
    path('entries/<int:pk>/', FoodEntryDetailView.as_view(), name='entry-detail'),
    path('entries/new/', FoodEntryCreateView.as_view(), name='entry-create'),
    path('entries/<int:pk>/update/', FoodEntryUpdateView.as_view(), name='entry-update'),
    path('entries/<int:pk>/delete/', FoodEntryDeleteView.as_view(), name='entry-delete'),
]
