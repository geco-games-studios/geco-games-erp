from rest_framework import serializers
from accounting.cash_management.models import CashManagement

class CashManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashManagement
        fields = '__all__'