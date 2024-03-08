from django.urls import path

from homework7 import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/', views.category, name="category"),

]