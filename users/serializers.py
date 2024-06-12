from rest_framework import serializers

from users.models import Payments, User


class PaymentsSerializer(serializers.Serializer):
    """Класс сериализатора для модели Payments"""
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели User"""
    class Meta:
        model = User
        fields = "__all__"
