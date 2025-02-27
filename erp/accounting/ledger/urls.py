from django.urls import path
from . import views

urlpatterns = [
    #accounts
    path('accounts/', views.ledger_account_list, name='ledger_account_list'),
    path('accounts/<int:pk>/', views.ledger_account_detail, name='ledger_account_detail'),
    path('accounts/new/', views.ledger_account_create, name='ledger_account_create'),
    path('accounts/<int:pk>/edit/', views.ledger_account_update, name='ledger_account_update'),
    path('accounts/<int:pk>/delete/', views.ledger_account_delete, name='ledger_account_delete'),
    #transcations
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/new/', views.transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    path('entries/', views.transaction_entry_list, name='transaction_entry_list'),
    path('entries/<int:pk>/', views.transaction_entry_detail, name='transaction_entry_detail'),
    path('entries/new/<int:transaction_id>/', views.transaction_entry_create, name='transaction_entry_create'),
    # Financial Reports URLs
    path('reports/', views.financial_reports, name='financial_reports'),  # Main reports page
    path('reports/trial-balance/', views.trial_balance, name='trial_balance'),  # Trial Balance report
    path('trial-balance/delete/', views.trial_balance_delete, name='trial_balance_delete'),
    path('reports/income-statement/', views.income_statement, name='income_statement'),  # Income Statement report
    path('reports/balance-sheet/', views.balance_sheet, name='balance_sheet'),  # Balance Sheet report
]