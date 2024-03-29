from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from django.utils import timezone

class Lead(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 254)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    #phone_number = PhoneField(blank=True, help_text='Contact phone number')

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Lead, self).save(*args, **kwargs)
