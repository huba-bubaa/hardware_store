import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hardware_store.settings')

import django

django.setup()

from django.contrib.auth.models import Group


GROUPS = ['cashier', 'accountant', 'shop_assistant']
MODELS = ['staff']
# создаем группы для Staff-a
for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
