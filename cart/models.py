from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination

# Create your models here.
class CartItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)


    def subtotal(self):
        return self.quantity * self.destination.price

