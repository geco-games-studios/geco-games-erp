from django.db import models
from accounting.ledger.models import LedgerAccount

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('trial_balance', 'Trial Balance'),
        ('income_statement', 'Income Statement'),
        ('balance_sheet', 'Balance Sheet'),
        ('cash_flow', 'Cash Flow'),
    ]
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    period = models.CharField(max_length=255)  # e.g., "Q1 2023", "2023"
    total_debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    net_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    total_assets = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    total_liabilities = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    total_equity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} - {self.period}"
