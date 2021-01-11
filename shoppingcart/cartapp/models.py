from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=150)
    ImageLink = models.FileField()
    Price = models.FloatField()
    Created_At = models.DateField(auto_now_add=True, null=True)
    Updated_At = models.DateField(auto_now=True, null=True)

    def _str_(self):
        return f"{self.id}{self.Title}"


class Order(models.Model):
    PAYMENT = (
        ('cash', 'Cash_OnDelivery'),
        ('paytm', 'Paytm_bank'),
        ('card', 'card_type'),

    )
    STATUS = (
        ('new', 'New_status'),
        ('paid', 'Paid_status'),

    )
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Total = models.IntegerField(default=0)
    Created_At = models.DateField(auto_now_add=True, null=True)
    Updated_At = models.DateField(auto_now=True, null=True)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    Status = models.CharField(
        choices=STATUS,
        max_length=30,
    )
    Mode_of_payment = models.CharField(
        choices=PAYMENT,
        max_length=30,
    )

    def _str_(self):
        return f'{self.id}-{self.UserId}-{self.Total}-{self.Created_At}{self.Updated_At}{self.Status}{self.Mode_of_payment}'


class OrderItem(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    OrderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Price = models.FloatField(default=0)

    def _str_(self):
        return f'{self.UserId}{self.OrderId}{self.ProductId}{self.Quantity}{self.Price}'
