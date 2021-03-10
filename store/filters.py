from django_filters import rest_framework as filters
from .models import Orders


# класс фильтрации заказов по дате
class OrdersFilter (filters.FilterSet):
    order_datetime_gth = filters.DateTimeFilter(field_name='order_datetime', lookup_expr='gt')
    order_datetime_lth = filters.DateTimeFilter(field_name='order_datetime', lookup_expr='lt')

    class Meta:
        model = Orders
        fields = ['order_datetime_gth', 'order_datetime_lth']