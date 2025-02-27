from rest_framework import viewsets, filters, pagination
from django.shortcuts import get_object_or_404
from accounting.reporting.models import Report
from .serializers import ReportSerializer
from accounting.ledger.models import LedgerAccount, TransactionEntry
from accounting.cash_management.models import CashManagement
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['report_type', 'period']
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['get'])
    def trial_balance(self, request):
        accounts = LedgerAccount.objects.all()
        trial_balance_data = []
        total_debit = 0
        total_credit = 0

        for account in accounts:
            debit_entries = TransactionEntry.objects.filter(account=account).aggregate(total_debit=Sum('debit'))['total_debit'] or 0
            credit_entries = TransactionEntry.objects.filter(account=account).aggregate(total_credit=Sum('credit'))['total_credit'] or 0
            balance = debit_entries - credit_entries
            trial_balance_data.append({
                'account': account.name,
                'debit': debit_entries,
                'credit': credit_entries,
                'balance': balance
            })
            total_debit += debit_entries
            total_credit += credit_entries

        report = Report.objects.create(
            report_type='trial_balance',
            period='Current Period',  # Update this as needed
            total_debit=total_debit,
            total_credit=total_credit
        )

        return Response({
            'trial_balance_data': trial_balance_data,
            'total_debit': total_debit,
            'total_credit': total_credit,
            'report_id': report.id
        })

    @action(detail=False, methods=['get'])
    def income_statement(self, request):
        revenue_accounts = LedgerAccount.objects.filter(name__icontains='Revenue')
        expense_accounts = LedgerAccount.objects.filter(name__icontains='Expense')
        
        total_revenue = TransactionEntry.objects.filter(account__in=revenue_accounts, credit__gt=0).aggregate(total=Sum('credit'))['total'] or 0
        total_expenses = TransactionEntry.objects.filter(account__in=expense_accounts, debit__gt=0).aggregate(total=Sum('debit'))['total'] or 0
        
        net_income = total_revenue - total_expenses

        report = Report.objects.create(
            report_type='income_statement',
            period='Current Period',  # Update this as needed
            total_revenue=total_revenue,
            total_expenses=total_expenses,
            net_income=net_income
        )
        
        return Response({
            'total_revenue': total_revenue,
            'total_expenses': total_expenses,
            'net_income': net_income,
            'report_id': report.id
        })

    @action(detail=False, methods=['get'])
    def balance_sheet(self, request):
        assets_accounts = LedgerAccount.objects.filter(name__icontains='Asset')
        liabilities_accounts = LedgerAccount.objects.filter(name__icontains='Liability')
        equity_accounts = LedgerAccount.objects.filter(name__icontains='Equity')
        
        total_assets = TransactionEntry.objects.filter(account__in=assets_accounts, debit__gt=0).aggregate(total=Sum('debit'))['total'] or 0
        total_liabilities = TransactionEntry.objects.filter(account__in=liabilities_accounts, credit__gt=0).aggregate(total=Sum('credit'))['total'] or 0
        total_equity = TransactionEntry.objects.filter(account__in=equity_accounts, credit__gt=0).aggregate(total=Sum('credit'))['total'] or 0

        report = Report.objects.create(
            report_type='balance_sheet',
            period='Current Period',  # Update this as needed
            total_assets=total_assets,
            total_liabilities=total_liabilities,
            total_equity=total_equity
        )
        
        return Response({
            'total_assets': total_assets,
            'total_liabilities': total_liabilities,
            'total_equity': total_equity,
            'report_id': report.id
        })

    @action(detail=False, methods=['get'])
    def cash_flow(self, request):
        cash_inflows = CashManagement.objects.filter(transaction_type='deposit').aggregate(total=Sum('amount'))['total'] or 0
        cash_outflows = CashManagement.objects.filter(transaction_type='withdrawal').aggregate(total=Sum('amount'))['total'] or 0
        net_cash_flow = cash_inflows - cash_outflows

        report = Report.objects.create(
            report_type='cash_flow',
            period='Current Period',  # Update this as needed
            total_revenue=cash_inflows,
            total_expenses=cash_outflows,
            net_income=net_cash_flow
        )
        
        return Response({
            'cash_inflows': cash_inflows,
            'cash_outflows': cash_outflows,
            'net_cash_flow': net_cash_flow,
            'report_id': report.id
        })