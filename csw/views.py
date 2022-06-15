from rest_framework import generics
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .serializers import *

from .models import *
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .forms import CswForm
from .forms import Work_contactForm, educationForm, pst5Form, charfForm, pracForm, privForm, profileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
# from tablib import Dataset
from django.http import HttpResponse
# from .resources import PersonResource
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@login_required()
def form1(request):
    forms = CswForm(instance=Csw)
    if request.method == "POST":
        forms = CswForm(request.POST, request.FILES,instance=Csw)
        if forms.is_valid():
            forms.save()
            messages.success(request, f'You have successfully added your first form..Please Complete Registration!!!')
            request.session['forward'] = True
            return redirect('work_contact')
    else:
        forms = CswForm()
    return render(request, 'users/form1.html', {'forms': forms})
    
@login_required()
def work_contact(request):
    if request.method == "POST":
        work_forms = Work_contactForm(request.POST)
        if work_forms.is_valid():
            work_forms.save()
            messages.success(request, f'You have successfully added your second form..Please Complete Registration!!!')
            request.session['forward'] = True
            return redirect('edu')
    else:
        work_forms = Work_contactForm()
        

    return render(request, 'users/work_contact.html', {'work_forms': work_forms})
    
@login_required()
def edu(request):
    if request.method == "POST":
        edu_forms  = educationForm(request.POST, request.FILES,instance=education_and_training)
        if edu_forms.is_valid():
            edu_forms.save()
            messages.success(request, f'You have successfully added your third form..Please Complete Registration!!!')
            return redirect('pst5')
    else:
        edu_forms = educationForm()
        

    return render(request, 'users/edu.html', {'edu_forms': edu_forms})

@login_required()    
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

@login_required()
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

@login_required()
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

@login_required()
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
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    return redirect('loginPage')

# @login_required()
# @allowed_users(allowed_roles=['user']
def profile(request):
    customer = request.user.customer
    profileforms = profileForm(instance=customer)

    if request.method == 'POST':
        profileforms = profileForm(request.POST, request.FILES,instance=customer)
        if profileforms.is_valid():
            profileforms.save()
            
    context = {'profileforms':profileforms}
    return render(request, 'users/profile.html', context)




#Serializers
class CswList(generics.CreateAPIView):
    serializer_class = CswSerializer

    def get_queryset(self):
        queryset = Csw.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class CswDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Csw.objects.all()
    serializer_class = CswSerializer

class Work_contactList(generics.CreateAPIView):
    serializer_class = Work_contactSerializer

    def get_queryset(self):
        queryset = Work_contact.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class Work_contactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work_contact.objects.all()
    serializer_class = Work_contactSerializer

class CustomerList(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class education_and_trainingList(generics.CreateAPIView):
    serializer_class = education_and_trainingSerializer

    def get_queryset(self):
        queryset = education_and_training.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class education_and_trainingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = education_and_training.objects.all()
    serializer_class = education_and_trainingSerializer

class pst_five_workList(generics.CreateAPIView):
    serializer_class = pst_five_workSerializer

    def get_queryset(self):
        queryset = pst_five_work.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class pst_five_workDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pst_five_work.objects.all()
    serializer_class = pst_five_workSerializer

class practise_outsideList(generics.CreateAPIView):
    serializer_class = practise_outsideSerializer

    def get_queryset(self):
        queryset = practise_outside.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class practise_outsideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = practise_outside.objects.all()
    serializer_class = practise_outsideSerializer

class character_refList(generics.CreateAPIView):
    serializer_class = character_refSerializer

    def get_queryset(self):
        queryset = character_ref.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class character_refDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = character_ref.objects.all()
    serializer_class = character_refSerializer

class rivate_practiceList(generics.CreateAPIView):
    serializer_class = rivate_practiceSerializer

    def get_queryset(self):
        queryset = rivate_practice.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class rivate_practiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = rivate_practice.objects.all()
    serializer_class = rivate_practiceSerializer

class UserList(generics.ListCreateAPIView):
    serializer_class = UserRegisterSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    

