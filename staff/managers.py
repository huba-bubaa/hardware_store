from django.contrib.auth.base_user import BaseUserManager


# создаем кастомный менеджер для Staff
class StaffManager(BaseUserManager):

    def create_user(self, email, password, groups, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        if not password:
            raise ValueError('Password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, groups=groups, **extra_fields)
        user.set_password(password)
        user.save()
        return user
