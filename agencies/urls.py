from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add-branch', views.createAgencyBranch, name='add-branch'),
    path('add-branch-admin', views.createAgencyBranchAdmin, name='add-branch-admin'),
    path('list-branch-admin', views.listBranchAdmin, name='list-branch-admin'),
    path('add-ticket-teller', views.createTicketTeller, name='add-ticket-teller'),
    path('list-tellers', views.listTicketTeller, name='list-tellers'),
    path('add-bus-layout', views.createBusLayout, name='add-bus-layout'),
    path('add-bus', views.createBus, name='add-bus'),
    path('list-buses', views.listBus, name='list-buses'),
    path('add-driver', views.addDrivers, name='add-driver'),
    path('list-drivers', views.listDrivers, name='list-drivers'),
    path('add-trip', views.addTrip, name='add-trip'),
    # path('customers/', include(('customers.urls', 'customers'), namespace='customers') ),
]