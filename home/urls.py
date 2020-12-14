from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("result", views.result, name="result"),
    path("index", views.index, name="index")

]