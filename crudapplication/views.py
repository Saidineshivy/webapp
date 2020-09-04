import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render,redirect
from crudapplication.forms import EmployeeForm
from crudapplication.models import Employee

def create(request):
    json_body=json.loads(request.body.decode('utf-8'))
    print("+++++++++++",json_body)
    emp_obj=Employee(**json_body)
    data = dict()
    records = []
    if request.method == "POST":
        emp_obj.save()
        employees = Employee.objects.all()
        for record in employees.values():
            records.append( record )
    else:
        return {"message":"please send proper data"}
    data["message"] = "Employee Created Succefflly".format( id )
    data['employees'] = records
    return JsonResponse(data=data)
    # return render(request, "index.html", {'form':form})

def show(request):
    employees = Employee.objects.all()
    data=dict()
    records = []
    for record in employees.values():
        records.append(record)
    data['employees']=records

    return JsonResponse(data=data)
    # return render(request,"show.html",{'employee': employees})

# def edit(request, id):
#     employee =Employee.objects.get(id=id)
#     return render(request,"edit.html",{'employee' : employee})
def update(request,pk):
    json_body = json.loads( request.body.decode( 'utf-8' ) )
    print(json_body)
    employee = Employee.objects.get(id=pk)
    emp_dict=model_to_dict(employee)
    print("DB details",emp_dict)
    emp_dict.update(json_body)
    print( "dict update ",emp_dict )
    emp_obj = Employee(**emp_dict)
    data = dict()
    records = []
    if request.method == "PUT":
        emp_obj.save()
        employees = Employee.objects.all()
        for record in employees.values():
            records.append( record )
    else:
        return {"message": "please send proper data"}
    data["message"] = "Employee Updated Succefflly".format( id )
    data['employees'] = records
    return JsonResponse( data=data )
    # return render(request, "index.h
def delete(request, pk):
    emp_obj= Employee.objects.get(id=pk)
    records=[]
    data=dict()
    if request.method == "DELETE":
        emp_obj.delete()
        employees = Employee.objects.all()
        for record in employees.values():
            records.append( record )

    else:
        return {"message": "please send proper data"}
    data["message"] = "Employee Deleted Succefflly".format(id)
    data['employees'] = records
    return JsonResponse( data=data )