from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys
from django.views.generic import TemplateView

 from django.shortcuts import render  
from django.http import HttpResponse  
from wsinterfaceproject.functions.functions import handle_uploaded_file  
from wsinterfaceproject.form import UploadFile  

# Create your views here.

def button(request):
    return render(request , 'home.html')

def home(request):
    return render(request , 'home.html')

def EPMFileUpload(request):
   return render(request, "EPMFileUpload.html")

def output(request):
    data = requests.get("https://reqres.in/api/users")    
    print(data.text)
    data = data.text
    return render(request , 'home.html' , {'data' : data})

def external(request):
    inp = request.POST.get('fileupload') 
    run([sys.executable , 'BreakSingleVideotoFrames.py', inp] ,shell=False ,stdout = PIPE) 
   # out = "file submitted Successfully"
    return render(request , 'home.html' )
    
    
   
def index(request):  
    if request.method == 'POST':  
        uploadFile = UploadFile(request.POST, request.FILES)  
        if uploadFile.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        uploadFile = UploadFile()  
        return render(request,"EPMFileUpload.html",{'form':uploadFile})  
