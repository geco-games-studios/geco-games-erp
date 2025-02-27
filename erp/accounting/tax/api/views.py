from django.http import Http404
from rest_framework import viewsets, filters, pagination
from django.shortcuts import get_object_or_404
from accounting.tax.models import TaxManagement
from .serializers import TaxManagementSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaxManagementViewSet(viewsets.ModelViewSet):
    queryset = TaxManagement.objects.all()
    serializer_class = TaxManagementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tax_name', 'description']
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
        serializer = TaxManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, id=None):
        tax_management =  get_object_or_404(self.queryset, (id))
        obj = self.serializer(tax_management, data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data)
        return Response(obj.errors, status=400)

    def destroy(self, request, id=None):
        tax_management = get_object_or_404(self.queryset, (id))
        tax_management.delete()
        return Response(status=204)