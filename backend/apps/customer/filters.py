import django_filters

from apps.customer.models import Customer


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['name']
