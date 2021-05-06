from django.db import models
from users.models import User
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=50, unique=True)
    company_token = models.CharField(max_length=400, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='usercompany')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Company, self).save(*args, **kwargs)
