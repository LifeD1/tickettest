from django.http import HttpResponse
from django.shortcuts import render, redirect
from agencies.forms import AddBrandAdminForm, AddBrandForm, AddBusForm, AddBusLayoutForm, AddDriverForm, AddTellerForm, AddTripForm
from agencies.models import Bus, Bus_layout, Driver, Trip
from sub_admins.models import Agency, Branche, User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def home(request):
    return render(request, 'agencies/branch_admins_dashboard.html')

def restricted(request):
    return render(request, 'agencies/restricted.html')
# @user_passes_test(user.groups == '')
def group_check(user):
    # if user.groups.filter(name='agency_admins').exists():
    #     return user.groups =="agency_admins"
    # else:
    #     return HttpResponse("You are not authorized to view this page.", status=403)
    if user.groups.filter(name='agency_admins').exists():
        print(user.groups)
        return True

@login_required
@user_passes_test(group_check, login_url='not_authorized')  
def createAgencyBranch(request):
    uagency = request.user.agency
    # print(agency)
    if request.method == 'POST':
        form = AddBrandForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.agency = uagency
            branch.save()

            return redirect('..')
    else:
        form = AddBrandForm()
    context = {'form':form}
    return render(request, 'agencies/add_branch.html', context)



def createAgencyBranchAdmin(request):
    uagency = request.user.agency
    if request.method =='POST':
        form = AddBrandAdminForm(request.POST)
        if form.is_valid():
            admingroup = 'branch_admins'
            group = Group.objects.get(name=admingroup)
            user = form.save(commit=False)
            user.agency = uagency
            user.save()
            user.groups.add(group)
            return redirect('list-branch-admin')
    else:
        form = AddBrandAdminForm()
        form.fields['branch'].queryset = Branche.objects.filter(agency=request.user.agency)
    context = {'form':form}
    return render(request, 'agencies/add_branch_admin.html', context)



def listBranchAdmin(request):
    bAdmin = User.objects.filter(groups__name='branch_admins')
    branches = Branche.objects.all()
    context = {'bAdmin':bAdmin, 'branches':branches}
    return render(request, 'agencies/list_branch_admins.html', context)

def listBranch(request):
    # bAdmin = User.objects.all()
    branches = Branche.objects.all()
    context = { 'branches':branches}
    return render(request, 'agencies/list_branches.html', context)


def createTicketTeller(request):
    uagency = request.user.agency
    if request.method =='POST':
        form = AddTellerForm(request.POST)
        if form.is_valid():
            admingroup = 'ticket_tellers'
            group = Group.objects.get(name=admingroup)
            user = form.save(commit=False)
            user.agency = uagency
            user.save()
            user.groups.add(group)
            return redirect('list-tellers')
    else:
        form = AddTellerForm()
        form.fields['branch'].queryset = Branche.objects.filter(agency=request.user.agency)
    context = {'form':form}
    return render(request, 'agencies/add_ticket_teller.html', context)

def listTicketTeller(request):
    tellers = User.objects.filter(groups__name='ticket_tellers')
    branches = Branche.objects.all()
    context = {'tellers':tellers, 'branches':branches}
    return render(request, 'agencies/list_tellers.html', context)


def createBusLayout(request):
    if request.method == 'POST':
        form = AddBusLayoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-buses')
    else:
        form = AddBusLayoutForm()
    context = {'form':form}
    return render(request, 'agencies/add_bus_layout.html', context)


def createBus(request):
    if request.method == 'POST':
        form = AddBusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-buses')
    else:
        form = AddBusForm()
    context = {'form':form}
    return render(request, 'agencies/add_bus.html', context)

def listBusLayout(request):
    context = {}
    return render(request, 'agencies/list_buses.html', context)


def listBus(request):
    buslayouts= Bus_layout.objects.all()
    buses = Bus.objects.all()
    context = {'buslayouts':buslayouts, 'buses':buses}
    return render(request, 'agencies/list_buses.html', context)


def addDrivers(request):
    if request.method == 'POST':
        user_agency = request.user.agency
        form = AddDriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.agency = user_agency
            driver.save()
            return redirect('list-drivers')
    else:
        form = AddDriverForm()
    context = {'form':form}
    return render(request, 'agencies/add_driver.html', context)

def listDrivers(request):
    # agency = Agency.objects.all()
    drivers = Driver.objects.all()
    context = {'drivers':drivers}
    return render(request, 'agencies/list_drivers.html', context)

def addTrip(request):
    user_agency = request.user.agency
    if request.method == 'POST':
        form = AddTripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.agency = user_agency
            trip.save()
    else:
        form = AddTripForm()
    context = {'form':form}
    form.fields['branch'].queryset = Branche.objects.filter(agency=request.user.agency)
    form.fields['bus'].queryset = Bus.objects.filter(agency=request.user.agency)
    return render(request, 'agencies/add_trip.html', context)

def listTrip(request):    
    trips = Trip.objects.all()
    context = {'trips':trips}
    return render(request, 'agencies/list_trips.html', context)