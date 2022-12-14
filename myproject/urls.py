from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('employee_detail/<int:employee_id>', views.employee_detail, name="employee_detail"),
]
