from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Sum
from django.shortcuts import render
from .models import FoodEntry
from .forms import FoodEntryForm, DateFilterForm
from datetime import date

class HomeView(TemplateView):
    template_name = 'tracker/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get today's entries
        today = date.today()
        today_entries = FoodEntry.objects.filter(date_consumed=today)
        
        # Calculate total calories for today
        total_calories = today_entries.aggregate(Sum('calories'))['calories__sum'] or 0
        
        # Get a summary of recent days with total calories
        daily_summary = FoodEntry.objects.values('date_consumed').annotate(
            total=Sum('calories')
        ).order_by('-date_consumed')[:7]  # Last 7 days with entries
        
        context.update({
            'today': today,
            'today_entries': today_entries,
            'total_calories': total_calories,
            'daily_summary': daily_summary,
        })
        
        return context

class FoodEntryListView(ListView):
    model = FoodEntry
    context_object_name = 'entries'
    template_name = 'tracker/entry_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Handle date filter
        filter_form = DateFilterForm(self.request.GET or None)
        context['filter_form'] = filter_form
        
        if filter_form.is_valid() and filter_form.cleaned_data.get('date'):
            filter_date = filter_form.cleaned_data.get('date')
            context['filter_date'] = filter_date
            
            # Calculate total calories for filtered date
            total_calories = self.get_queryset().aggregate(Sum('calories'))['calories__sum'] or 0
            context['total_calories'] = total_calories
            
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Apply date filter if present
        filter_form = DateFilterForm(self.request.GET or None)
        if filter_form.is_valid() and filter_form.cleaned_data.get('date'):
            filter_date = filter_form.cleaned_data.get('date')
            queryset = queryset.filter(date_consumed=filter_date)
            
        return queryset

class FoodEntryDetailView(DetailView):
    model = FoodEntry
    context_object_name = 'entry'
    template_name = 'tracker/entry_detail.html'

class FoodEntryCreateView(CreateView):
    model = FoodEntry
    form_class = FoodEntryForm
    template_name = 'tracker/entry_form.html'
    success_url = reverse_lazy('entry-list')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['date_consumed'] = date.today()
        return initial

class FoodEntryUpdateView(UpdateView):
    model = FoodEntry
    form_class = FoodEntryForm
    template_name = 'tracker/entry_form.html'
    success_url = reverse_lazy('entry-list')

class FoodEntryDeleteView(DeleteView):
    model = FoodEntry
    context_object_name = 'entry'
    template_name = 'tracker/entry_confirm_delete.html'
    success_url = reverse_lazy('entry-list')
