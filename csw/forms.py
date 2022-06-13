from cProfile import label
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email',  'password1', 'password2']

class CswForm(ModelForm):
    class Meta:
        model = Csw
        fields = ['title','first_name',  'surname', 'date_of_birth', 'nationality', 'national_id_number', 'country_of_birth', 'city','Gender', 'house_number','mobile_number', 'passport_pho',]

class Work_contactForm(ModelForm):
    class Meta:
        model = Work_contact
        fields = "__all__"

class educationForm(ModelForm):
    class Meta:
        model = education_and_training
        fields = ['title_of_your_training','start_date',  'end_date', 'name_of_provider', 'certificates','city', 'country', 'name','job_title', 'telephone_number','email', 'title_of_your_training1','start_date1','end_date1','name_of_pro','address','town','country1',]

class pst5Form(ModelForm):
    class Meta:
        model = pst_five_work
        fields = "__all__"
        
class charfForm(ModelForm):
    class Meta:
        model = character_ref
        fields = "__all__"
        
class pracForm(ModelForm):
    class Meta:
        model = practise_outside
        fields = ['country_of_practise','regulatory_body',  'regulatory_number', 'organisation', 'start_date', 'end_date', 'post', 'address','city', 'country','name_of_manager', 'mobile_number','email','any_discipinary']

class privForm(ModelForm):
    class Meta:
        model = rivate_practice
        fields = "__all__"

class profileForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['user']

class PersonData(forms.Form):
	class meta:
		model = Person
		fields = '__all__'
        
        