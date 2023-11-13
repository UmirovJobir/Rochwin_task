from django.contrib import admin
from .models import (
    Employee,
    Client,
    Product,
    Order,
)

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)