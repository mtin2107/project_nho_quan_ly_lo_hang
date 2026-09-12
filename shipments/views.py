from rest_framework import viewsets

from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    Tự động có: GET /shipments/ (list), POST /shipments/ (create),
    GET /shipments/{id}/ (retrieve), PUT/PATCH /shipments/{id}/ (update),
    DELETE /shipments/{id}/ (destroy).
    """
    queryset = Shipment.objects.all().order_by("-created_at")
    serializer_class = ShipmentSerializer
