from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .pdf import generate_invoice_pdf
from rest_framework.decorators import api_view

# Create your views here.

from rest_framework import generics
from .models import Customer, Invoice
from .serializers import CustomerSerializer, InvoiceSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class InvoiceListCreate(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetail(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

@api_view(['GET'])
def download_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return generate_invoice_pdf(invoice)
