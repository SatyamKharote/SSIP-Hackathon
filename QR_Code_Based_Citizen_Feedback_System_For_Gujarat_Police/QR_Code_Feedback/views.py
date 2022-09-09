from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# login function
def login(request):
    return render(request, 'QR_Code_Feedback/login.html')


def otp(request):
    return render(request, 'QR_Code_Feedback/otp.html')


def home(request):
    return render(request, 'QR_Code_Feedback/home.html')
