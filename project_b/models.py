from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
class License(models.Model):
    start_date = models.DateField()
    validity_months= models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])  # Restrict to 1-12 months
    device_id = models.CharField(max_length=100)
    server_ip = models.CharField(max_length=100)
    nmssecuritykey = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=17)

    def __str__(self):
        return f"License for {self.device_id}"

def clean(self):
        if self.validity_months > 12:
            raise ValidationError({'validity_months': 'Month not valid. Must be between 1 and 12.'})