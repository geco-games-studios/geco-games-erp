from django.db import models
from accounting.ledger.models import LedgerAccount

class AssetManagement(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    purchase_date = models.DateField()
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.asset_name} - {self.purchase_amount}"
