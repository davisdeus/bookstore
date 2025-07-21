from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer
