from django.http import Http404
from rest_framework import viewsets, filters, pagination
from django.shortcuts import get_object_or_404
from accounting.cash_management.models import CashManagement
from .serializers import CashManagementSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CashManagementViewSet(viewsets.ModelViewSet):
    queryset = CashManagement.objects.all()
    serializer_class = CashManagementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'transaction_type']
    pagination_class = StandardResultsSetPagination
    
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        cash_management = self.get_object(pk)
        serializer = self.serializer_class(cash_management, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        cash_management = self.get_object(pk)
        cash_management.delete()
        return Response(status=204)