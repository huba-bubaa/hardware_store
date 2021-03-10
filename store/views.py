import datetime

from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Products, Orders, Account
from .serializers import ProductSerializer, OrdersSerializer, AccountSerializer
from datetime import date
from dateutil.relativedelta import relativedelta
from .filters import OrdersFilter
from staff.permissions import CashierPermission, ShopAssistantPermission, AccountantPermission
from django_filters import rest_framework as filters


# проверяет необходимость начисления скидки и высчитывает сумму со скидкой. вызывается при создании обьекта
def count_discount(price, delivery):
    date_del = datetime.datetime.strptime(delivery, '%Y-%m-%d')
    if date_del.date() + relativedelta(months=+1) < date.today():
        return [20, int(price) - (int(price) * 20 / 100)]
    return [0, price]


# вью для просмотра, добавления, удаления, редактирования
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        price = self.request.data['price']
        delivery = self.request.data['delivery_date']
        count = count_discount(price, delivery)
        serializer.save(discount=count[0], price_with_discount=count[1])


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = OrdersFilter

    def get_permissions(self):
        if self.request.user.groups == Group.objects.get(name='cashier'):
            self.permission_classes = [CashierPermission, ]
        elif self.request.user.groups == Group.objects.get(name='shop_assistant'):
            self.permission_classes = [ShopAssistantPermission, ]
        else:
            self.permission_classes = [AccountantPermission, ]
        return super().get_permissions()

    def perform_create(self, serializer):
        if self.request.user.groups == Group.objects.get(name='cashier') \
                and self.request.data['status'] == 'performed':
            raise ValueError('Only shop assistant can perform the order!')
        super(OrderViewSet, self).perform_create(serializer)

    def perform_update(self, serializer):
        if self.request.user.groups == Group.objects.get(name='cashier') \
                and self.request.data['status'] == 'performed':
            raise ValueError('Only shop assistant can perform the order!')
        elif self.request.user.groups == Group.objects.get(name='shop_assistant') \
                and self.request.data['status'] != 'performed':
            raise ValueError('Only cashier can set this status!')
        super(OrderViewSet, self).perform_update(serializer)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [CashierPermission, ]
