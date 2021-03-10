from django.db import models

ADDED = 'added'
PERFORMED = 'performed'
PAID = 'paid'
STATUS = [
    (ADDED, 'added'),
    (PERFORMED, 'performed'),
    (PAID, 'paid')
]


# модель продуктов, содержит название, дату доставки, цену, скидку и цену со скидкой.
# скидка и цена со скидкой расчитываются автоматически при post запросе на соответствующий viewset
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    delivery_date = models.DateField()
    discount = models.IntegerField(default=0)
    price = models.IntegerField()
    price_with_discount = models.IntegerField(null=True)

    def __str__(self):
        return self.product_name


# модель заказов, содержит ссылку на продукт, дату заказа и статус заказа(добавлен, обработан,
# оплачен)
class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_datetime = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.product_id.product_name + '  Order date: ' + str(self.order_datetime) \
               + '  Status:' + self.status


# модель счетов, содержит ссылку на заказ и время оформления счета
class Account (models.Model):
    order_id = models.OneToOneField(Orders, on_delete=models.CASCADE)
    account_datetime = models.DateTimeField()

    def __str__(self):
        return self.order_id + ' ' + self.account_datetime
