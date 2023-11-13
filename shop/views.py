import json
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, response, status
from .models import (
    Employee,
    Client,
    Product,
    Order,
)

class EmployeeDetailStatistics(views.APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        month = request.query_params.get('month')
        year = request.query_params.get('year')

        orders = employee.order_employee.filter(date__year=year, date__month=month)
        
        clients = []
        products_count = 0
        price = 0

        if orders:
            for order in orders:
                clients.append(order.client)
                products_count += len(order.products.all())
                price += order.price
            
            clients_count = len(set(clients))

            data = {
                "employee": employee.full_name,
                "clients": clients_count,
                "products": products_count,
                "price": price
            }
        else:
            data = {
                    "employee": employee.full_name,
                    "clients": 0,
                    "products": 0,
                    "price": 0
                }

        return response.Response(data, status=status.HTTP_200_OK)
    

class EmployeeListStatistics(views.APIView):
    def get(self, request):
        employees = Employee.objects.all()

        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not employees.exists():
            return response.Response({"message": "Employees not found"}, status=status.HTTP_200_OK)

        employees_data = []

        for employee in employees:
            orders = employee.order_employee.filter(date__year=year, date__month=month)
            
            clients = []
            products_count = 0
            price = 0

            if orders:
                for order in orders:
                    clients.append(order.client)
                    products_count += len(order.products.all())
                    price += order.price
                
                clients_count = len(set(clients))

                data = {
                    "id": employee.pk,
                    "employee": employee.full_name,
                    "clients": clients_count,
                    "products": products_count,
                    "price": price
                }
                employees_data.append(data)
            else:
                data = {
                    "id": employee.pk,
                    "employee": employee.full_name,
                    "clients": 0,
                    "products": 0,
                    "price": 0
                }
                employees_data.append(data)

        return response.Response(employees_data, status=status.HTTP_200_OK)


class ClientDetailStatistics(views.APIView):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)

        month = request.query_params.get('month')
        year = request.query_params.get('year')

        orders = client.order_client.filter(date__year=year, date__month=month)
        
        products_count = 0
        price = 0

        if orders:
            for order in orders:
                products_count += len(order.products.all())
                price += order.price
            
            data = {
                "client": client.full_name,
                "products": products_count,
                "price": price
            }
        else:
            data = {
                    "client": client.full_name,
                    "products": 0,
                    "price": 0
                }

        return response.Response(data, status=status.HTTP_200_OK)

