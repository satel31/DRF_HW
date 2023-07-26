from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.courses.models import Payment
from apps.courses.serializers.payment import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """View to get a list of payments.
       Has filter (by course, lesson and method of payment) and ordering (by payment_date).
       In case of the tests don't forget to change permissions."""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['payment_date']
    filterset_fields = ('course', 'lesson', 'method',)
    permission_classes = [IsAuthenticated]
    # In case of test
    #permission_classes = [AllowAny]


class PaymentDetailAPIView(generics.RetrieveAPIView):
    """View to get a particular of payment.
       In case of the tests don't forget to change permissions."""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    # In case of test
    #permission_classes = [AllowAny]
