# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import LedgerAccount, Transaction, TransactionEntry
from .forms import LedgerAccountForm, TransactionForm, TransactionEntryForm
from django.db import models
from django.db.models import Sum

def ledger_account_list(request):
    accounts = LedgerAccount.objects.all()
    return render(request, 'ledger_account_list.html', {'accounts': accounts})

def ledger_account_detail(request, pk):
    account = get_object_or_404(LedgerAccount, pk=pk)
    return render(request, 'ledger_account_detail.html', {'account': account})

def ledger_account_create(request):
    if request.method == 'POST':
        form = LedgerAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger_account_list')
    else:
        form = LedgerAccountForm()
    return render(request, 'ledger_account_form.html', {'form': form})

def ledger_account_update(request, pk):
    account = get_object_or_404(LedgerAccount, pk=pk)
    if request.method == 'POST':
        form = LedgerAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('ledger_account_detail', pk=account.pk)
    else:
        form = LedgerAccountForm(instance=account)
    return render(request, 'ledger_account_form.html', {'form': form})

def ledger_account_delete(request, pk):
    account = get_object_or_404(LedgerAccount, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('ledger_account_list')
    return render(request, 'ledger_account_confirm_delete.html', {'account': account})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
        else:
            print(form.errors)  
    else:
        form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transaction_confirm_delete.html', {'transaction': transaction})

def transaction_entry_list(request):
    entries = TransactionEntry.objects.all()
    return render(request, 'transaction_entry_list.html', {'entries': entries})

def transaction_entry_detail(request, pk):
    entry = get_object_or_404(TransactionEntry, pk=pk)
    transaction_entries = TransactionEntry.objects.filter(transaction=entry.transaction)
    total_debit = transaction_entries.aggregate(total_debit=Sum('debit'))['total_debit'] or 0
    total_credit = transaction_entries.aggregate(total_credit=Sum('credit'))['total_credit'] or 0
    return render(request, 'transaction_entry_detail.html', {
        'entry': entry,
        'transaction_entries': transaction_entries,
        'total_debit': total_debit,
        'total_credit': total_credit,
        'transaction': entry.transaction  # Include the transaction details
    })

def transaction_entry_create(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionEntryForm(request.POST, transaction=transaction)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.transaction = transaction
            entry.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionEntryForm(transaction=transaction)
    return render(request, 'transaction_entry_form.html', {'form': form, 'transaction': transaction})


def financial_reports(request):
    return render(request, 'financial_reports.html')

def trial_balance(request):
    accounts = LedgerAccount.objects.all()
    trial_balance_data = []
    total_debit = 0
    total_credit = 0

    for account in accounts:
        debit_entries = TransactionEntry.objects.filter(account=account).aggregate(total_debit=Sum('debit'))['total_debit'] or 0
        credit_entries = TransactionEntry.objects.filter(account=account).aggregate(total_credit=Sum('credit'))['total_credit'] or 0
        balance = debit_entries - credit_entries
        trial_balance_data.append({
            'account': account,
            'debit': debit_entries,
            'credit': credit_entries,
            'balance': balance
        })
        total_debit += debit_entries
        total_credit += credit_entries

    return render(request, 'trial_balance.html', {
        'trial_balance_data': trial_balance_data,
        'total_debit': total_debit,
        'total_credit': total_credit
    })
    
    
def trial_balance_delete(request):
    if request.method == 'POST':
        TransactionEntry.objects.all().delete()
        return redirect('trial_balance')
    return render(request, 'trial_balance_confirm_delete.html')

def income_statement(request):
    revenue_accounts = LedgerAccount.objects.filter(name__icontains='Revenue')
    expense_accounts = LedgerAccount.objects.filter(name__icontains='Expense')
    
    total_revenue = TransactionEntry.objects.filter(account__in=revenue_accounts, credit__gt=0).aggregate(total=Sum('credit'))['total'] or 0
    total_expenses = TransactionEntry.objects.filter(account__in=expense_accounts, debit__gt=0).aggregate(total=Sum('debit'))['total'] or 0
    
    net_income = total_revenue - total_expenses
    
    return render(request, 'income_statement.html', {
        'total_revenue': total_revenue,
        'total_expenses': total_expenses,
        'net_income': net_income
    })

def balance_sheet(request):
    assets_accounts = LedgerAccount.objects.filter(name__icontains='Asset')
    liabilities_accounts = LedgerAccount.objects.filter(name__icontains='Liability')
    equity_accounts = LedgerAccount.objects.filter(name__icontains='Equity')
    
    total_assets = TransactionEntry.objects.filter(account__in=assets_accounts, debit__gt=0).aggregate(total=Sum('debit'))['total'] or 0
    total_liabilities = TransactionEntry.objects.filter(account__in=liabilities_accounts, credit__gt=0).aggregate(total=Sum('credit'))['total'] or 0
    total_equity = TransactionEntry.objects.filter(account__in=equity_accounts, credit__gt=0).aggregate(total=Sum('credit'))['total'] or 0
    
    return render(request, 'balance_sheet.html', {
        'total_assets': total_assets,
        'total_liabilities': total_liabilities,
        'total_equity': total_equity
    })