from django.db import models
from accounting.ledger.models import LedgerAccount

class ExpenseManagement(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=255)
    expense_date = models.DateField()
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.expense_name} - {self.expense_amount}"
