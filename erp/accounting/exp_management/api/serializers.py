from rest_framework import serializers
from accounting.exp_management.models import ExpenseManagement

class ExpenseManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseManagement
        fields = '__all__'