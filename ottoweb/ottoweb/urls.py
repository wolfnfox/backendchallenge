"""ottoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ottoapi import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/assigncar/<int:car_id>'+\
                      '/<str:with_option>'+\
                      '/<int:assign_id>/',views.AssignCar.as_view()),
    path('api/branch/',views.BranchList.as_view()),
    path('api/branch/<int:branch_id>/',views.BranchDetail.as_view()),
    path('api/car/',views.CarList.as_view()),
    path('api/car/<int:car_id>/',views.CarDetail.as_view()),
    path('api/driver/',views.DriverList.as_view()),
    path('api/driver/<int:driver_id>/',views.DriverDetail.as_view()),
]
