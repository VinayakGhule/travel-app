from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('packages/',views.packages, name='packages'),    
    path('packages/<int:package_id>/',views.package_detail, name='package_detail'),    


]