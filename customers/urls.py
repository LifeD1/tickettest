from django.urls import path

import agencies
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.customerRegistration, name = 'register'),
    path('login/', views.userLogin, name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('customer-dashboart/', views.dashboard, name = 'customer-dashboard'),
]