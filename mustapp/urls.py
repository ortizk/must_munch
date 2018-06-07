from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seattle/', views.categories, name='categories'),
    path('seattle/<option_cat>/', views.options, name='options'),
    # path('seattle/<option_cat>/upvote/<rest_id>/', views.upvote, name='upvote'),
    path('seattle/drinks/vote/<int:rest_id>/', views.vote, name='vote'),
    path('seattle/eats/vote/<int:rest_id>/', views.vote, name='vote'),
    path('seattle/datenight/vote/<int:rest_id>/', views.vote, name='vote'),

]
