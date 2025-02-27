from django.db import models
from accounting.ledger.models import LedgerAccount

class Compliance(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    compliance_name = models.CharField(max_length=255)
    compliance_date = models.DateField()
    compliance_status = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.compliance_name} - {self.compliance_status}"

class AuditTrail(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    action_date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.action} - {self.user} - {self.action_date}"
