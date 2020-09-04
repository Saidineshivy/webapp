from django.contrib import admin
from crudapplication.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','eemail','econtact']
admin.site.register(Employee,EmployeeAdmin)