from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from django.db.models import Q
from datetime import datetime
from .models import Business, Type, Ledger, Head, Mode, Transaction
from .serializers import (
    BusinessSerializer, TypeSerializer, LedgerSerializer,
    HeadSerializer, ModeSerializer, TransactionSerializer
)

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

class HeadViewSet(viewsets.ModelViewSet):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer