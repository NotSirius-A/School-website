from django.urls import path
from django.contrib.auth import authenticate

from . import views

urlpatterns = [
    path('login/', views.login_page_view, name='login_page')
]
