from django.urls import path
from accounting.ledger.api.views import LedgerAccountViewSet, TransactionViewSet, TransactionEntryViewSet, FinancialReportsViewSet
from accounting.cash_management.api.views import CashManagementViewSet
from accounting.exp_management.api.views import ExpenseManagementViewSet
from accounting.compliance.api.views import ComplianceViewSet, AuditTrailViewSet
from accounting.reporting.api.views import ReportViewSet
from accounting.budgeting.api.views import BudgetViewSet
from accounting.tax.api.views import TaxManagementViewSet
from accounting.asset_management.api.views import AssetManagementViewSet

urlpatterns = [
    # Ledger Accounts
    path('accounts', LedgerAccountViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('accounts/<int:pk>', LedgerAccountViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Transactions
    path('transactions', TransactionViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('transactions/<int:pk>', TransactionViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Transaction Entries
    path('entries', TransactionEntryViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('entries/<int:pk>', TransactionEntryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Financial Reports
    path('financial-reports', FinancialReportsViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('financial-reports/<int:pk>', FinancialReportsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Cash Management
    path('cash-management', CashManagementViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('cash-management/<int:pk>', CashManagementViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Expense Management
    path('expense-management', ExpenseManagementViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('expense-management/<int:pk>', ExpenseManagementViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Compliance
    path('compliance', ComplianceViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('compliance/<int:pk>', ComplianceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Audit Trail
    path('audit-trail', AuditTrailViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('audit-trail/<int:pk>', AuditTrailViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    # Reporting Module
    path('reports', ReportViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('reports/<int:pk>', ReportViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('reports/trial-balance', ReportViewSet.as_view({
        'get': 'trial_balance',
    }), name='trial_balance'),
    path('reports/income-statement', ReportViewSet.as_view({
        'get': 'income_statement',
    }), name='income_statement'),
    path('reports/balance-sheet', ReportViewSet.as_view({
        'get': 'balance_sheet',
    }), name='balance_sheet'),
    path('reports/cash-flow', ReportViewSet.as_view({
        'get': 'cash_flow',
    }), name='cash_flow'),

    # Budget
    path('budget', BudgetViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('budget/<int:pk>', BudgetViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),

    # Tax Management
    path('tax-management', TaxManagementViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('tax-management/<int:pk>', TaxManagementViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),

    # Asset Management
    path('asset-management', AssetManagementViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('asset-management/<int:pk>', AssetManagementViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),
]