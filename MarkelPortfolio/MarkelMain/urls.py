from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstPage, name="home"),
    path('about-me', views.about, name="about"),
    # path('createtask', views.create, name="createtask"),
]