from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    


class BookingTable(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    booking_date = models.DateField()