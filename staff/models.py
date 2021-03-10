from django.contrib.auth.models import AbstractUser, Group
from .managers import StaffManager
from django.db import models


# создаем модель юзера(Staff) для которого username будет email. В settings прописали AUTH_USER_MODEL
# поле Username убираем
class Staff(AbstractUser):
    username = None
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True, verbose_name="email")
    staff_name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['groups_id']

    objects = StaffManager()

    def __str__(self):
        return self.email
