from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

# dashboard
def dashboard(request):
    return render(request, 'dashboard.html') 


def report(request):
    return render(request, 'report.html')   


def qr_code(request):
    return render(request, 'qr_code.html') 


def create_user(request):
    return render(request, 'create_user.html') 

def change_password(request):
    return render(request, 'change_pasword.html')
