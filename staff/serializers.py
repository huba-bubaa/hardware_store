from rest_framework.serializers import ModelSerializer
from .models import Staff


# создаем свой сериалайзер для деталей user профайла
class StaffSerializer(ModelSerializer):

    class Meta:
        model = Staff
        fields = ['id', 'email', 'groups', 'staff_name']

    def create(self, validated_data):
        user = Staff.objects.create(**validated_data)
        user.is_staff = True
        user.save()

        return user

