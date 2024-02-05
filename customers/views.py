from django.shortcuts import render, redirect
from customers.forms import CustomerRegistrationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

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

        return render(request, 'sub_admins/index.html')
    elif request.user.groups.filter(name='agency_admins').exists():
        return render(request, 'agencies/index.html')
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
    
    return render(request, 'customers/customer-dashboard.html')