from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def phone_number_verify(request):
    return render(request, 'firebase_opt_system.html')

def loginadmin(request):
    return render(request, 'loginadmin.html')

def index(request):
    return render(request, 'dashboard.html')

# dashboard
def dashboard(request):
    return render(request, 'dashboard.html') 

def add_question(request):
    return render(request, 'add_question.html')

def report(request):
    return render(request, 'report.html')   


def qr_code(request):
    return render(request, 'qr_code.html') 


def create_user(request): 
    return render(request, 'create_user.html') 

def change_password(request):
    return render(request, 'change_pasword.html')

def abc(request): 
    data1=request.GET.get('text1') 
    data2=request.GET.get('text2') 
    data3=request.GET.get('text3')  

    return render(request, 'change_pasword.html') 

def save_data(request):
    pass
