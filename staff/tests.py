from django.contrib.auth.models import Group
from django.test import TestCase
from django.contrib.auth import get_user_model


# тестируем правильность создания юзера через менеджер
class StaffTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        # если в тестовой бд нет групп, добавляем их
        if not Group.objects.all():
            GROUPS = ['cashier', 'accountant', 'shop_assistant']
            for group in GROUPS:
                new_group, created = Group.objects.get_or_create(name=group)
        staff = User.objects.create_user(email='test@user.com', password='test', staff_name='Test Name',
                                         groups=Group.objects.get(name='cashier'))
        self.assertEqual(staff.email, 'test@user.com')
        self.assertEqual(staff.groups, Group.objects.get(name='cashier'))
        self.assertTrue(staff.is_active)
