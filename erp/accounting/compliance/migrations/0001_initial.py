# Generated by Django 5.1.2 on 2025-02-27 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditTrail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('action_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.ledgeraccount')),
            ],
        ),
        migrations.CreateModel(
            name='Compliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compliance_name', models.CharField(max_length=255)),
                ('compliance_date', models.DateField()),
                ('compliance_status', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.ledgeraccount')),
            ],
        ),
    ]
