from django.shortcuts import render, get_object_or_404, redirect
from .models import BudgetForecast
from .forms import BudgetForecastForm

def budget_forecast_list(request):
    forecasts = BudgetForecast.objects.all()
    return render(request, 'budget_forecast_list.html', {'forecasts': forecasts})

def budget_forecast_create(request):
    if request.method == 'POST':
        form = BudgetForecastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_forecast_list')
    else:
        form = BudgetForecastForm()
    return render(request, 'budget_forecast_form.html', {'form': form})

def budget_forecast_update(request, pk):
    forecast = get_object_or_404(BudgetForecast, pk=pk)
    if request.method == 'POST':
        form = BudgetForecastForm(request.POST, instance=forecast)
        if form.is_valid():
            form.save()
            return redirect('budget_forecast_list')
    else:
        form = BudgetForecastForm(instance=forecast)
    return render(request, 'budget_forecast_form.html', {'form': form})
