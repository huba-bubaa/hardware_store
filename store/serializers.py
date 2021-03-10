from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Products, Orders, Account


# Сериалайзер для модели продуктов, определяет скидку и цену со скидкой как readOnly поля
class ProductSerializer(HyperlinkedModelSerializer):
    discount = serializers.ReadOnlyField()
    price_with_discount = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = ['id', 'url', 'product_name', 'price', 'discount', 'price_with_discount', 'delivery_date']


# Сериалайзер для модели заказов
class OrdersSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Orders
        fields = ['id', 'url', 'product_id', 'order_datetime', 'status']


# Сериалайзер для модели счетов, определяет дополнительное поле - конечная стоимость(со скидкой)
class AccountSerializer (HyperlinkedModelSerializer):
    result_cost = serializers.IntegerField(source='order_id.product_id.price_with_discount', read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'url', 'order_id', 'result_cost', 'account_datetime']
