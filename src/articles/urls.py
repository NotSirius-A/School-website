from django.urls import path

from . import views

url_base = 'article/'

urlpatterns = [
        path('', views.article_list_view, name='article_list'),
        path(url_base+'<slug:slug>/', views.article_entire_view, name='article_entire'),
        path(url_base+'submit/form/', views.article_form_view, name='article_form')
]
