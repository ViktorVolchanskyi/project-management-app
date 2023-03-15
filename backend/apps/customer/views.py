from rest_framework import viewsets

from apps.customer.models import Customer
from apps.customer.serilaizers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
