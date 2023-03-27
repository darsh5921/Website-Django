from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def index (request):
    # return HttpResponse("This is home page")
    # context={
    # "variable":"this is a variable value string passed from template to view"
    # }
    # messages.success(request,"Test Message")
    return render(request,'index.html')
def about (request):
    return render(request,'about.html')

def services (request):
    return render(request,'service.html')

def contact (request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        add=request.POST.get('add')
        contact=Contact(name=name,email=email,phno=phno,add=add,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details Have been saved !.')
    return render(request,'contact.html')

