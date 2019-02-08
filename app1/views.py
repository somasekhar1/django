import csv
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee
def showindex(request):
    emp=Employee.objects.all()
    return render(request,"index.html",{"employee":emp})


def savesetails(request):
    id=request.POST.get("t1")
    name=request.POST.get("t2")
    dob=request.POST.get("t3")
    doj=request.POST.get("t4")
    gender=request.POST.get("t5")
    designition=request.POST.get("t6")
    contact=request.POST.get("t7")
    email=request.POST.get("t8")
    salery=request.POST.get("t9")
    image=request.FILES["t10"]
    Employee(id=id,name=name,dob=dob,doj=doj,gender=gender,designition=designition,contact=contact,email=email,salery=salery,image=image).save()
    return render(request,"index.html",{"msg":"data saved"})


def viewdetails(request):
    id=request.POST.get("t1")
    emp=Employee.objects.filter(id=id).all()
    return render(request,"viewdetails.html",{"data":emp})


def deletedetails(request):
    delete = request.POST.get("t2")
    emp = Employee.objects.filter(id=delete).all()
    return render(request,"deletedetails.html",{"datas":emp})


def deletes(request):
    delid=request.POST.get("del_id")
    Employee.objects.filter(id=delid).delete()
    emp=Employee.objects.all()
    return render(request,"index.html",{"employee":emp})


def updatedetails(request):
    uid=request.POST.get("u_id")
    Employee.objects.filter(id=uid).update()
    d1=Employee.objects.all()
    return render(request,"update.html",{"d2":d1})


def employeecsv(request):
    response=HttpResponse(content_type="text/csv")
    response["content-disposition"]="atachment";filename="employee/csv"
    wr=csv.writer(response)
    emp=Employee.objects.all()
    for x in emp:
        wr.writerow([x.id,x.name,x.dob,x.doj,x.gender,x.designition,x.contact,x.email,x.salery,x.image])
    return response