from django.urls import path
from . import views

urlpatterns = [
    path('budget-forecast/', views.budget_forecast_list, name='budget_forecast_list'),
    path('budget-forecast/new/', views.budget_forecast_create, name='budget_forecast_create'),
    path('budget-forecast/<int:pk>/edit/', views.budget_forecast_update, name='budget_forecast_update'),
]