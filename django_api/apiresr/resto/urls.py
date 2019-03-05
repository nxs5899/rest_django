
from django.urls import path, include
from . import views


urlpatterns = [
    path('invoices', views.invoice_list),
    path('invoices/<int:pk>/', views.get_invoice)
  ]
