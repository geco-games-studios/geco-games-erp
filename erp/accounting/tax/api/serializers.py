from rest_framework import serializers
from accounting.tax.models import TaxManagement

class TaxManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxManagement
        fields = '__all__'