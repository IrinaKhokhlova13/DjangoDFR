from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    """
    Контроллер списка платежей
    """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('data_payment',)