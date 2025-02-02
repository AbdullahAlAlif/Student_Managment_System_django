from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Students
from .forms  import StudentForm

# Create your views here.
def index(request):
    return render(request,'students\index.html',{
                     'Students' : Students.objects.all()
                  })

def view_student(request,id):
    Student = Students.Objects.get(pk=id)
    return HttpResponseRedirect(reverse('Students_index'))


def add(request):
    if request.method == "POST":
        form=StudentForm(request.POST) #it's a bound form which will validate the POST data first
        if form.is_valid():
            new_student_id = form.cleaned_data["Student_id"]
            new_first_name = form.cleaned_data["first_name"]
            new_last_name = form.cleaned_data["last_name"]
            new_email = form.cleaned_data["email"]
            new_department = form.cleaned_data["Department"]
            new_gpa = form.cleaned_data["gpa"]

            new_student = Students(
            Student_id=new_student_id,
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            Department=new_department,
            gpa=new_gpa
             )
            new_student.save() #we are saving the new student to db
            return render(request,'students/add.html',{
                            'form' : StudentForm(), 
                            'success' : True 
                          })
    else:
         return render(request,'students/add.html', {
                            'form' : StudentForm()
                          })


def edit (request, id):
    if request.method=="POST":
        Student = Students.objects.get(pk=id)
        form=StudentForm(request.POST,instance=Student) #we pass instance of Student to ensure we edit for the one we clicked for
        if form.is_valid():
            form.save() #we are saving the new form (edited) for that instance
            return render(request,'students/edit.html',{
                            'form' : form, 
                            'success' : True 
                          })
    else:
        Student = Students.objects.get(pk=id)
        form=StudentForm(instance=Student)  #Only pass instance, no POST data***
        return render(request,'students/edit.html', {
                            'form' : form #we are passing the form for the instance not the form structure StudentForm() since we are editing 
                          })


def delete (request, id):
    if request.method=="POST":
        Student = Students.objects.get(pk=id)
        Student.delete() #Just simply Delete the record from database
        return HttpResponseRedirect(reverse('Students_index'))
     
    