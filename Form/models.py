from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Lead(TimeStampMixin):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 254)
    phone_number = PhoneNumberField()
    #date = models.DateTimeField(auto_now_add=True)
