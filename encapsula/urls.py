from django.urls import path
from .views import CustomerCreateAPIView, CustomerUpdateAPIView




urlpatterns = [
    path('customers/create/', CustomerCreateAPIView.as_view(), name='customer-create'),
    path('customers/<int:pk>/update/', CustomerUpdateAPIView.as_view(), name='customer-update'),
]
