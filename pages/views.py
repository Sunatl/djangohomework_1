from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .form import *

def get_all(request):
    tasks = Cars.objects.all()
    return render(request,"index.html",context={"tasks":tasks})

def get_all_carr(request):
    tasks = Cars.objects.all()
    return render(request,"index11.html",context={"tasks":tasks})


def get_by_id(request,pk):
    tasks  = Cars.objects.filter(id=pk).first()
    if tasks:
        return render(request,"index1.html",context={"tasks":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add(request):
    if request.method == "POST":
        form  = Tasksform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("get_all")
    else:
        form = Tasksform()
    return render(request,"index3.html", context={"form":form})



def update(request,pk):
    tasks  = Cars.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Tasksform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("get_all")
        else:
            form = Tasksform(instance=tasks)
            
        return render(request,"index4.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete(request,pk):
    tasks =  Cars.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("get_all")
        else:
            return render(request,"delete.html",context={"tasks":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
# Company


def get_company(request):
    tasks = Company.objects.all()
    return render(request,"index5.html",context={"tasks":tasks})


def get_by_company(request,pk):
    tasks  = Company.objects.filter(id=pk).first()
    if tasks:
        return render(request,"index6.html",context={"tasks":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add_company(request):
    if request.method == "POST":
        form  = Companyform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("get_all")
    else:
        form = Companyform()
    return render(request,"index7.html", context={"form":form})



def update_company(request,pk):
    tasks  = Company.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Companyform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("get_all")
        else:
            form = Companyform(instance=tasks)
            
        return render(request,"index8.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete_company(request,pk):
    tasks =  Company.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("get_company")
        else:
            return render(request,"delete1.html",context={"tasks":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
        
    
 
    


