from rest_framework import serializers
from accounting.asset_management.models import AssetManagement

class AssetManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetManagement
        fields = '__all__'