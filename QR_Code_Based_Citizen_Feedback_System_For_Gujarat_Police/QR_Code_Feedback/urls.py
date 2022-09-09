from django.urls import path
from QR_Code_Feedback import views


urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('otp', views.otp),
]
