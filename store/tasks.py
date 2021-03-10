from datetime import date

from celery.schedules import crontab
from hardware_store.celery_app import app
from dateutil.relativedelta import relativedelta

from .models import Products
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# Celery task, выбирает записи продуктов у которых дата доставки > месяца назад, прописывает скидку 20% и
# цену со скидкой. Далее ищет записи где price_with_discount = null и устанавливает им значение price
# (в случае если запись была создана с помощью фикстур)
@app.task(name='store.tasks.discount_check')
def discount_check():
    date_eq = date.today() - relativedelta(months=+1)
    products = Products.objects.filter(delivery_date__lte=date_eq)
    for product in products:
        if product.discount == 0:
            product.discount = 20
            product.price_with_discount = int(product.price) - (int(product.price) * 20 / 100)
            product.save()
            logger.info("Updated product: "+product.product_name)

    products = Products.objects.filter(price_with_discount=None)
    for product in products:
        product.price_with_discount = product.price
        product.save()
