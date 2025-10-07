from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=2, decimal_places=2)


    def __str__(self):
        return f"Order {self.id}  by {self.user.username}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=2, decimal_places=2)