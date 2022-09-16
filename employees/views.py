import employees
from django.shortcuts import render
from django.http import Http404
from .models import Employee

# Create your views here.

def home(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, "home.html", context)

def employee_detail(request, employee_id):
    try:
       employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee not found')
    context = {'employee': employee}
    return render(request, "employee_detail.html", context)

 