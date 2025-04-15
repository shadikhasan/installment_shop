from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
    
    path('installments/next-due/', NextDueInstallmentView.as_view(), name='next-due-installment'),
    path('installments/', AllInstallmentsView.as_view(), name='all-installments'),
    path('installments/pay/<int:installment_id>/', PayInstallmentView.as_view(), name='pay-installment'),
    
    path('purchases/', views.PurchaseListView.as_view()),
    path('purchases/my/', views.MyPurchaseListView.as_view()),
    path('purchases/create/', views.PurchaseCreateView.as_view()),
    
    path('reports/weekly/', views.WeeklyReportView.as_view()),
    path('reports/monthly/', views.MonthlyReportView.as_view()),
]
