from django.db import models
from accounting.ledger.models import LedgerAccount

class BudgetForecast(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    period = models.CharField(max_length=255) 
    budgeted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forecasted_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.account.name} - {self.period}"
