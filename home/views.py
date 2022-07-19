
from django.shortcuts import render
from . models import *
from .forms import Book
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def book(request):
    if request.method == "POST":
        form = Book(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirm.html')
    form = Book()
    dictform ={
        'form': form
    }
    return render(request, 'book.html', dictform)
def doctors(request):
    doct={
        'doctors':Doctors.objects.all(),
    }
    return render(request, 'doctors.html', doct)
def contact(request):
    return render(request, 'contact.html')
def department(request):
    dept_dict={
        'dept':Departments.objects.all()
    }
    return render(request, 'departments.html', dept_dict)