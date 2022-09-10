from django.urls import path

from office_view import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard), 
    path('report', views.report),
    path('qr_code', views.qr_code),
    path('create-user', views.create_user),
    path('change-password', views.change_password) 
]
