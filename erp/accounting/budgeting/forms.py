from django import forms
from .models import BudgetForecast

class BudgetForecastForm(forms.ModelForm):
    class Meta:
        model = BudgetForecast
        fields = ['account', 'period', 'budgeted_amount', 'actual_amount', 'forecasted_amount', 'description']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border-2 border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:border-blue-500',
                'placeholder': f'Enter {field.label}'
            })