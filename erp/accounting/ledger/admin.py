# admin.py

from django.contrib import admin
from .models import LedgerAccount, Transaction, TransactionEntry

@admin.register(LedgerAccount)
class LedgerAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'balance')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search on name field

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'reference')  # Fields to display in the list view
    search_fields = ('description', 'reference')  # Enable search on description and reference fields
    ordering = ('-date',)  # Order transactions by date (latest first)

@admin.register(TransactionEntry)
class TransactionEntryAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'account', 'debit', 'credit')  # Fields to display in the list view
    list_filter = ('transaction', 'account')  # Enable filtering by transaction and account
    search_fields = ('account__name',)  # Enable search on account name

