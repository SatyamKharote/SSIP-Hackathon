from django.urls import path
from QR_Code_Feedback import views


urlpatterns = [
    path('', views.home),
    path('login/',views.loginuser, name='loginuser'),
    path('otp/', views.otp, name='otp'),
    path('feedback/', views.feedback, name='feedback'),
]
