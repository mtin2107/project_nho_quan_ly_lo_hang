from django.db import models


class Shipment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
    ]
    MODE_CHOICES = [
        ("air", "Air"),
        ("sea", "Sea"),
        ("road", "Road"),
    ]

    tracking_code = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance_km = models.FloatField()
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    weight_kg = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tracking_code} ({self.origin} -> {self.destination})"
