# Generated by Django 5.1.2 on 2025-02-27 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('trial_balance', 'Trial Balance'), ('income_statement', 'Income Statement'), ('balance_sheet', 'Balance Sheet')], max_length=50)),
                ('period', models.CharField(max_length=255)),
                ('total_debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_revenue', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('total_expenses', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('net_income', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('total_assets', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('total_liabilities', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('total_equity', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LedgerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='ledger.ledgeraccount')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='ledger.transaction')),
            ],
        ),
    ]
