from django.db import models
from accounting.ledger.models import LedgerAccount

class CashManagement(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    transaction_type_choices = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    transaction_type = models.CharField(max_length=50, choices=transaction_type_choices)

    def __str__(self):
        return f"{self.account.name} - {self.transaction_type} - {self.amount}"
