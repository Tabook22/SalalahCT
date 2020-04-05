from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("add_app/",include("apps.app_form.urls")),
    path('admin/', admin.site.urls),
]
