from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add-agency', views.addAgency, name = 'add-agency'),
    path('add-agency-admin', views.createAgencyAdmin, name='add-agency-admin'),
     path('list-agencies', views.agencyList, name = 'list-agencies'),
]