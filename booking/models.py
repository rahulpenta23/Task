from django.db import models

# Create your models here.

class Slot(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    is_booked = models.BooleanField(default=False)

    class Meta:
        db_table = "booking_slot"
    