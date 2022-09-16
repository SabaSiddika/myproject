from django.contrib import admin
from .models import AvailableJobs, Employee

# Register your models here.
@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'phone_num']
admin.site.register(AvailableJobs)
