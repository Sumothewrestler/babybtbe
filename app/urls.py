from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BusinessViewSet, TypeViewSet, LedgerViewSet,
    HeadViewSet, ModeViewSet, TransactionViewSet
)

router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'types', TypeViewSet)
router.register(r'ledgers', LedgerViewSet)
router.register(r'heads', HeadViewSet)
router.register(r'modes', ModeViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]