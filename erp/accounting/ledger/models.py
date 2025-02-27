from django.db import models

class LedgerAccount(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.description}"

class TransactionEntry(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='entries', on_delete=models.CASCADE)
    account = models.ForeignKey(LedgerAccount, related_name='entries', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # New field for entry title
    description = models.TextField(blank=True, null=True)  # New field for entry description
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.account.name} - {self.title} - Debit: {self.debit}, Credit: {self.credit}"

class FinancialReport(models.Model):
    report_type_choices = [
        ('trial_balance', 'Trial Balance'),
        ('income_statement', 'Income Statement'),
        ('balance_sheet', 'Balance Sheet'),
    ]
    report_type = models.CharField(max_length=50, choices=report_type_choices)
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
