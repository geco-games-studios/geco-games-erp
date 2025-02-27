from rest_framework import serializers
from accounting.ledger.models import FinancialReport, LedgerAccount, Transaction, TransactionEntry

class LedgerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionEntry
        fields = '__all__'
        
class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'