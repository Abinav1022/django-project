from django.contrib import admin
from django.urls import path
from abinavapp import views
urlpatterns = [
    path('loginPage/', views.loginPage),
]
