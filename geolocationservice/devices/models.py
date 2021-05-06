from django.db import models
from companies.models import Company


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    deviceid = models.IntegerField(blank=True, null=True, unique=True)
    device_model = models.CharField(max_length=255, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app = models.CharField(max_length=50, unique=False)
    version = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.device_model


class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                    null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f'{[self.latitude, self.longitude]!r}'
