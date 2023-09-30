from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, WalletViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
