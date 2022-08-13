
import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student
# Create your views here.
# function to add new student
def add(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = Student(name = nm, email= em, password = pw)
            reg.save()
        return HttpResponseRedirect('.')
    else:
        fm = StudentForm()
        stu =  Student.objects.all()
        return render(request,'add.html',{'form':fm,'stud':stu})

#This function is to Update or edit data
def update_data(request,id):
    if request.method == 'POST':
        p = Student.objects.get(pk = id)
        fm = StudentForm(request.POST, instance=p)
        if fm.is_valid():
            fm.save()
        
    else:
         p = Student.objects.get(pk = id)
         fm = StudentForm(instance=p)
    return render(request,'update.html',{'form':fm}) 


#function to delete student data
def delete_data(request,id):
    if request.method == 'POST':
        p = Student.objects.get(pk = id)
        p.delete()
        return HttpResponseRedirect('/')

    