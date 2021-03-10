from .views import *

from rest_framework.routers import DefaultRouter

store_urls = DefaultRouter()
store_urls.register(r'products', ProductViewSet)
store_urls.register(r'orders', OrderViewSet)
store_urls.register(r'accounts', AccountViewSet)

