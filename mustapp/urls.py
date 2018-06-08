from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
    path('seattle/', views.categories, name='categories'),
    path('seattle/<option_cat>/', views.options, name='options'),
    # path('seattle/<option_cat>/upvote/<rest_id>/', views.upvote, name='upvote'),
    path('seattle/drinks/vote/<int:rest_id>/', views.vote, name='vote'),
    path('seattle/eats/vote/<int:rest_id>/', views.vote, name='vote'),
    path('seattle/datenight/vote/<int:rest_id>/', views.vote, name='vote'),

]
