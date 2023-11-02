from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.login),
    path('admin', admin.site.urls),
]
