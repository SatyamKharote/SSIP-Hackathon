from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'QR_Code_Feedback/home.html') 


def self(request):
    return HttpResponse("<h1> I am Satyam </h1>")