from django.urls import path

import agencies
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.customerRegistration, name = 'register'),
    path('login/', views.userLogin, name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('customer-dashboard/', views.customerDashbaord, name = 'customer-dashboard'),
    path('reservation/', views.ticketReservation, name = 'reservation'),
    path('get_branches/', views.get_branches, name = 'get_branches'),
    path('get_trip/', views.get_trip, name = 'get_trip'),
    path('get_booked_seats/', views.get_booked_seats, name='get_booked_seats'),
    path('all_av_trips/', views.listAllAvTrips, name='all_av_trips'),
    path('agency_av_trips/', views.listAvTripsOnAgency, name='agency_av_trips'),
    path('list_agency/', views.listcustAgencies, name='list_agency'),
    path('single-ag/<str:pk>/', views.singleAgPage, name='single-ag'),

]