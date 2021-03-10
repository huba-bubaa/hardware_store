from django.contrib.auth.models import Group
from rest_framework import permissions

from staff.models import Staff


# права доступа для касира
class CashierPermission(permissions.BasePermission):
    required_group = 'cashier'

    def has_permission(self, request, view):
        staff = Staff.objects.get(email=request.user.email)
        if staff.groups == Group.objects.get(name=self.required_group):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        staff = Staff.objects.get(email=request.user.email)
        if staff.groups == Group.objects.get(name=self.required_group):
            return True
        return False


# права доступа для продавца-консультанта
class ShopAssistantPermission(permissions.BasePermission):
    required_group = 'shop_assistant'

    def has_permission(self, request, view):
        staff = Staff.objects.get(email=request.user.email)
        if view.action in ['list', 'update', 'retrieve'] \
                and staff.groups == Group.objects.get(name=self.required_group):
            return True
        print(staff.groups)
        return False

    def has_object_permission(self, request, view, obj):
        staff = Staff.objects.get(email=request.user.email)
        if view.action in ['list', 'update', 'retrieve'] \
                and staff.groups == Group.objects.get(name=self.required_group):
            return True
        return False


# права доступа для бухгалтера
class AccountantPermission(permissions.BasePermission):
    required_group = 'accountant'

    def has_permission(self, request, view):
        staff = Staff.objects.get(email=request.user.email)
        if view.action in ['list'] \
                and staff.groups == Group.objects.get(name=self.required_group):
            return True
        print(staff.groups)
        return False

    def has_object_permission(self, request, view, obj):
        staff = Staff.objects.get(email=request.user.email)
        if view.action in ['list'] \
                and staff.groups == Group.objects.get(name=self.required_group):
            return True
        return False