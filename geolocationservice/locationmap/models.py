from django.db import models
from companies.models import Company
from devices.models import Device
from django.utils import timezone


class Locationmap(models.Model):
    latitude = models.DecimalField(max_digits=9,
                                   decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9,
                                    decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f'{[self.latitude, self.longitude]!r}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Locationmap, self).save(*args, **kwargs)
