from rest_framework import serializers
from accounting.budgeting.models import BudgetForecast

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetForecast
        fields = '__all__'