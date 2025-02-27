from django.urls import path, include

urlpatterns = [
    path('ledger/', include('accounting.ledger.urls')),
    # path('tax/', include('accounting.tax.urls')),
    # path('asset_management/', include('accounting.asset_management.urls')),
    path('budgeting/', include('accounting.budgeting.urls')),
    # path('compliance/', include('accounting.compliance.urls')),
    # path('exp_management/', include('accounting.exp_management.urls')),
    # path('reporting/', include('accounting.reporting.urls')),
    # path('cash_management/', include('accounting.cash_management.urls')),
]
