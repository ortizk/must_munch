from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seattle/', views.categories, name='categories'),
    path('seattle/<option_cat>/', views.options, name='options'),]
