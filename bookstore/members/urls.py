from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'), 
    path('addnew/', views.addnew, name='addnew'),  # Corrected URL pattern for the addnew view
    path('sin/', views.sin, name='sin'),
    path('shoping_basket/', views.shoping_basket, name='shoping_basket'),
    path('edit/', views.edit, name='edit'),  
]