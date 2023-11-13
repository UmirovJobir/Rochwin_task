from django.urls import path
from .views import (
    EmployeeDetailStatistics,
    EmployeeListStatistics,
    ClientDetailStatistics
)

urlpatterns = [
    path('statistics/employee/<int:pk>/', EmployeeDetailStatistics.as_view()),
    path('employee/statistics/', EmployeeListStatistics.as_view()),
    path('statistics/client/<int:pk>/', ClientDetailStatistics.as_view()),
]