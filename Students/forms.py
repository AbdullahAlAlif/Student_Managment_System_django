from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta: #internal Meta class of ModelForm where we give all the meta data for the form
        model=Students
        fields=['Student_id','first_name',"last_name","email","Department","gpa"]
        labels={
            "Student_id" : "Student ID" ,
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "email" : "E-mail",
            "Department" : "Department",
            "gpa" : "GPA"
        }
        widgets ={
            "Student_id" : forms.NumberInput(attrs={'class':'form-control'}),
            "first_name" : forms.TextInput(attrs={'class':'form-control'}),
            "last_name"  : forms.TextInput(attrs={'class':'form-control'}),
            "email"      : forms.EmailInput(attrs={'class':'form-control'}),
            "Department" : forms.TextInput(attrs={'class':'form-control'}),
            "gpa"        : forms.NumberInput(attrs={'class':'form-control'})
         }