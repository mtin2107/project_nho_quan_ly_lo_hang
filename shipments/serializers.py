from rest_framework import serializers

from .models import Shipment
from .utils import estimate_delivery_hours


class ShipmentSerializer(serializers.ModelSerializer):
    # Trường tính toán, không lưu trong DB — được thêm vào response lúc serialize
    estimated_delivery_hours = serializers.SerializerMethodField()

    class Meta:
        model = Shipment
        fields = [
            "id",
            "tracking_code",
            "origin",
            "destination",
            "distance_km",
            "mode",
            "weight_kg",
            "status",
            "created_at",
            "estimated_delivery_hours",
        ]
        read_only_fields = ["id", "created_at"]

    def get_estimated_delivery_hours(self, obj):
        return estimate_delivery_hours(obj.distance_km, obj.mode)
