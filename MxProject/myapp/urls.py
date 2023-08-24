from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('sign-up/',views.Register,name='Register'),
    path('login/',views.Login,name='Login'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('Logout/',views.Logout,name='Logout'),
]