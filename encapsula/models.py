from django.db import models
from basemodel.models import BaseModel
import inspect
from django.core.exceptions import ValidationError


class SecureCustomerManager(models.Manager):
    def create(self, *args, **kwargs):
        try:
           raise Exception("Customer obyektlari faqat CustomerService orqali yaratilishi kerak.")

        except Exception as e:
            return e




class Customer(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    objects = SecureCustomerManager()  # <-- create() endi bloklangan

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._allow_save = False  # faqat servis orqali saqlash mumkin

    def save(self, *args, **kwargs):
        if not self._allow_save:
            raise Exception("Customer obyektlarini faqat CustomerService orqali yarating.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.phone})"


