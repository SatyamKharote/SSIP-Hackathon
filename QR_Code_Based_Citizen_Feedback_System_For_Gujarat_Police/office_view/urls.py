from django.urls import path
from office_view import views


urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard)
]
