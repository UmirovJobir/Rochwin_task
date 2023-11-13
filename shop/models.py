from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self) -> str:
        return self.full_name

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self) -> str:
        return self.full_name

class Product(models.Model):
   name  = models.CharField(max_length=100)
   quantity = models.PositiveIntegerField()
   price = models.DecimalField(max_digits=10, decimal_places=2)

   def __str__(self) -> str:
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='order_client')
    products = models.ManyToManyField(Product, related_name='order_products')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='order_employee')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    