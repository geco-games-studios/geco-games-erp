from django.db import models
from accounting.ledger.models import LedgerAccount


class TaxManagement(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    tax_name = models.CharField(max_length=255)
    tax_date = models.DateField()
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tax_name} - {self.tax_amount}"
