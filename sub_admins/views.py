from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import AddAgencyForm, AddAgencyAdminForm
from .models import Agency, User
# Create your views here.
def home(request):
    return render(request, 'sub_admins/index.html')



def addAgency(request):
    
    if request.method == 'POST':
        form = AddAgencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agency-list')
    else:
        form = AddAgencyForm()

    return render(request, 'sub_admins/add_agency.html', {'form':form})

def createAgencyAdmin(request):
    
    if request.method == 'POST':
        form = AddAgencyAdminForm(request.POST)
        if form.is_valid():
            admingroup = 'sub_admins'
            group = Group.objects.get(name=admingroup)
            user = form.save()
            user.groups.add(group)
            return redirect('agency-list')
    else:
        form = AddAgencyAdminForm()

    context ={'form':form}
    return render(request, 'sub_admins/add_agency_admin.html', context)

def agencyList(request):
    agencies = Agency.objects.all()
    agencyAdmin = User.objects.all()

    context ={'agencies': agencies, 'agencyAdmin': agencyAdmin}
    return render(request, 'sub_admins/agency_list.html', context)
