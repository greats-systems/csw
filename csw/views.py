from http.client import HTTPResponse
from sqlite3 import register_adapter
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import *
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .forms import CswForm
from .forms import Work_contactForm, educationForm, pst5Form, charfForm, pracForm, privForm, profileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from .decorators import unauthenticated_user, allowed_users, admin_only


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hello!!! Your account was created successfully')
            return redirect('loginPage')
    else:
        form = UserRegisterForm()
        

    return render(request, 'users/register.html', {'form': form})

def loginPage(request):
    
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('form1')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'users/loginPage.html', context)


def form1(request):
    if request.method == "POST":
        forms = CswForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, f'You have successfully added your first form..Please Complete Registration!!!')
            return redirect('work_contact')
    else:
        forms = CswForm()
        

    return render(request, 'users/form1.html', {'forms': forms})
    

def work_contact(request):
    if request.method == "POST":
        work_forms = Work_contactForm(request.POST)
        if work_forms.is_valid():
            work_forms.save()
            messages.success(request, f'You have successfully added your second form..Please Complete Registration!!!')
            return redirect('edu')
    else:
        work_forms = Work_contactForm()
        

    return render(request, 'users/work_contact.html', {'work_forms': work_forms})
    

def edu(request):
    if request.method == "POST":
        edu_forms  = educationForm(request.POST)
        if edu_forms.is_valid():
            edu_forms.save()
            messages.success(request, f'You have successfully added your third form..Please Complete Registration!!!')
            return redirect('pst5')
    else:
        edu_forms = educationForm()
        

    return render(request, 'users/edu.html', {'edu_forms': edu_forms})
    
def pst5(request):
    if request.method == "POST":
        pst5_forms  = pst5Form(request.POST)
        if pst5_forms.is_valid():
            pst5_forms.save()
            messages.success(request, f'You have successfully added your fouth form..Please Complete Registration!!!')
            return redirect('charf')
    else:
        pst5_forms = pst5Form()
        

    return render(request, 'users/pst5.html', {'pst5_forms': pst5_forms})

def charf(request):
    if request.method == "POST":
        charf_forms  = charfForm(request.POST)
        if charf_forms.is_valid():
            charf_forms.save()
            messages.success(request, f'You have successfully added your fifth form..Please Complete Registration!!!')
            return redirect('pract')
    else:
        charf_forms = charfForm()
        

    return render(request, 'users/charf.html', {'charf_forms': charf_forms})

def pract(request):
    if request.method == "POST":
        pract_forms  = pracForm(request.POST)
        if pract_forms.is_valid():
            pract_forms.save()
            messages.success(request, f'You have successfully added your fifth form..Please Complete Registration!!!')
            return redirect('priv')
    else:
        pract_forms = pracForm()
        

    return render(request, 'users/pract.html', {'pract_forms': pract_forms})

def priv(request):
    if request.method == "POST":
        privt_forms  = privForm(request.POST)
        if privt_forms.is_valid():
            privt_forms.save()
            messages.success(request, f' Congradulations now you are registred!!!!!')
            return redirect('priv')
    else:
        privt_forms = privForm()
        

    return render(request, 'users/priv.html', {'privt_forms': privt_forms})
    # submitted = False
    # if request.method == "POST":
    #    privt_forms  = privForm(request.POST)
    #    if privt_forms .is_valid():
    #        privt_forms .save()
    #        return HttpResponseRedirect('/priv?submitted=true')
    
    # else:
    #    privt_forms = privForm
    #    if 'submitted' in request.GET:
    #        submitted=True
    #    return render(request, 'users/priv.html',{'privt_forms': privt_forms , 'submitted':submitted})

def logout(request):
    return redirect('loginPage')

@login_required()
# @allowed_users(allowed_roles=['user'])
def profile(request):
    customer = request.user.customer
    profileforms = profileForm(instance=customer)

    if request.method == 'POST':
        profileforms = profileForm(request.POST, request.FILES,instance=customer)
        if profileforms.is_valid():
            profileforms.save()
            
    context = {'profileforms':profileforms}
    return render(request, 'users/profile.html', context)
    
    

