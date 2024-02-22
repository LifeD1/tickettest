# import json
import itertools
from django.http import JsonResponse
from django.shortcuts import render, redirect
from agencies.models import Trip
from customers.forms import CustomerRegistrationForm, LoginForm, ReservationForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from customers.models import Reservation
from sub_admins.models import Agency, Branche, User
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'customers/index.html')


def customerRegistration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            usergroup = 'customers'
            group = Group.objects.get(name = usergroup)
            user = form.save()
            user.groups.add(group)
            login(request, user)
            return redirect('home')
    else:
        form = CustomerRegistrationForm()
    context = {'form':form}
    return render(request, 'customers/register.html', context)


def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'customers/login.html', context)

def userLogout(request):
    auth.logout(request)
    return redirect('login')




@login_required(login_url='login')
def dashboard(request):
    if request.user.groups.filter(name='sub_admins').exists():

        return render(request, 'sub_admins/sub_admins_dashboard.html')
    elif request.user.groups.filter(name='agency_admins').exists():
        return render(request, 'agencies/agency_admins_dashbord.html')
    elif request.user.groups.filter(name='branch_admins').exists():
        return render(request, 'agencies/branch_admins_dashboard.html')
    elif request.user.groups.filter(name='ticket_tellers').exists():
        return render(request, 'agencies/ticket_tellers_dashboard.html')
    elif request.user.groups.filter(name='customers').exists():
        return redirect('customer-dashboard')
    else:
        return redirect('login')
    # return render(request, 'travel/dashboard1.html')


def customerDashbaord(request):
    
    return render(request, 'customers/customer_dashboard.html')


def get_branches(request):
    agency_id = request.GET.get('agency_id')
    branches = Branche.objects.filter(agency_id=agency_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)

def get_trip(request):
    trips = Trip.objects.values_list('from_origin', flat=True) # Fetch your model instance
    for trip in trips:
        print(trip)
    return JsonResponse({'origins': list(trips)})

def get_booked_seats(request):
    booked_seats = Reservation.objects.values_list('seat_number', flat=True)
    return JsonResponse({'booked_seats': list(booked_seats)})



def ticketNumber(request):
    current_date = timezone.now()
    date_str = str(current_date.date()).replace("-","")
    selectedtrip = Trip.objects.get(trip_id = 1)
    agency = str(selectedtrip.agency)
    
    a_first_letters_list=[word[0] for word in agency.split()]
    a_first_letter = ''.join(map(str, a_first_letters_list))
    prifix = a_first_letter + date_str

    zfillprifix = "-"
    zfillprifix = zfillprifix.zfill(4)
    prifix = prifix+zfillprifix

    # print(prifix)

    last_record = Reservation.objects.filter(ticket_number__contains = a_first_letter).last()

    # new_tick_num = ''
    if last_record:
        #do somethin
        ticket_num = last_record.ticket_number
        #getting value after -
        suf = ticket_num.partition('-')[2]
        #removing leading zeros and increasing it by 1
        sufint = int(suf.lstrip('0')) + 1
        # concatinating with prefix to get new number
        new_tick_num = prifix+str(sufint)
    else:
        #start ticket number from 1
        new_tick_num = prifix+'1'
    return new_tick_num

   


def ticketReservation(request):
    # trips = None
    # current_date = None
    # selectedtrip = None
    ticket_num = ticketNumber(request)
    
    trips = Trip.objects.all()
    current_date = timezone.now()
    selectedtrip = Trip.objects.get(trip_id = 1)

    form = ReservationForm(request.POST)
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        # print (request.POST('first_name'))
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.ticket_number = ticket_num
            reserve.save()
            return redirect('dashboard')
    else:
        
        bus = selectedtrip.bus
        bus_type = selectedtrip.bus_type
        trip_cost = selectedtrip.trip_cost

        user = User.objects.get(id=request.user.id)
        first_name = user.first_name
        last_name = user.last_name
        id_card = user.id_card
        phone = user.phone     
        agency = user.agency

        user_dict = {
            'first_name': first_name,
            'last_name': last_name,
            'id_card': id_card,
            'phone': phone,
            'bus': bus,
            'bus_type': bus_type,
            'trip_cost': trip_cost, 
            'agency': agency, 
        }
        form = ReservationForm(initial=user_dict)
        # form.fields['branch'].queryset = Branche.objects.filter(agency=request.user.agency)
    context = {'form': form, 'trips': trips, 'current_date': current_date, 'selectedtrip':selectedtrip}
    return render(request, 'customers/reservation.html', context)


def listAllAvTrips(request):
    trips = Trip.objects.all()
    current_date = timezone.now()

    context = {'trips': trips, 'current_date': current_date}
    return render(request, 'customers/av_trips.html', context)


def listAvTripsOnAgency(request):
    trips = Trip.objects.all()
    agencies = Agency.objects.all()
    current_date = timezone.now()

    context = {'trips': trips, 'current_date': current_date, 'agencies':agencies}
    return render(request, 'customers/av_trips_per_agency.html', context)

def listcustAgencies(request):
    agencies = Agency.objects.all()
    trips = Trip.objects.all()
    current_date = timezone.now()
    
    context = {'agencies':agencies, 'current_date': current_date, 'trips': trips}
    return render(request, 'customers/list_agencies.html', context)


def singleAgPage(request, pk):
    agency = Agency.objects.get(id = pk)
    trips = Trip.objects.all()
    current_date = timezone.now()

    context = {'agency': agency, 'trips':trips, 'current_date': current_date}
    return render(request, 'customers/single_agency_trip.html', context )