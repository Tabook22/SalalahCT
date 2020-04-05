from django.urls import path,include
from .views import newApp

urlpatterns = [
    path("new_app",newApp, name="newApp"),
]
