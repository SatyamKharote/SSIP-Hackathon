from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# login function
def loginuser(request):
    return render(request, 'QR_Code_Feedback/loginuser.html');

# OTP function
def otp(request):
    return render(request, 'QR_Code_Feedback/otp.html')

def feedback(request):
    return render(request, 'QR_Code_Feedback/feedback.html')

def thankyou(request):
    return render(request, 'QR_Code_Feedback/thankyou.html')

def home(request):
    return render(request, 'QR_Code_Feedback/home.html')
