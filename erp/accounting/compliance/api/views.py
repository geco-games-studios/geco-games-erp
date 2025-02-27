from rest_framework import viewsets, filters, pagination
from django.shortcuts import get_object_or_404
from accounting.compliance.models import Compliance, AuditTrail
from .serializers import ComplianceSerializer, AuditTrailSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ComplianceViewSet(viewsets.ModelViewSet):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['compliance_name', 'description']
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ComplianceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        compliance = self.get_object(pk)
        serializer = ComplianceSerializer(compliance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        compliance = self.get_object(pk)
        compliance.delete()
        return Response(status=204)

class AuditTrailViewSet(viewsets.ModelViewSet):
    queryset = AuditTrail.objects.all()
    serializer_class = AuditTrailSerializer

    def list(self, request):
        queryset = AuditTrail.objects.all()
        serializer = AuditTrailSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuditTrailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        audit_trail = get_object_or_404(AuditTrail, pk=pk)
        serializer = AuditTrailSerializer(audit_trail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        audit_trail = get_object_or_404(AuditTrail, pk=pk)
        audit_trail.delete()
        return Response(status=204)