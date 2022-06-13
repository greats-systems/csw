from django.urls import path

from .serializers import CswSerializer
# from csw import views
from . import views
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('form1/', views.form1, name='form1'),
    path('work_contact/', views.work_contact, name='work_contact'),
    path('edu/', views.edu, name='edu'),
    path('pst5/', views.pst5, name='pst5'),
    path('charf/', views.charf, name='charf'),
    path('pract/', views.pract, name='pract'),
    path('priv/', views.priv, name='priv'),
    path('input/', views.input, name='input'),
    # serializers
    path('Csw/', CswList.as_view()),
    path('Csw/', CswDetail.as_view()),
    path('Work_contact1/', Work_contactList.as_view()),
    path('Work_contact1/', Work_contactDetail.as_view()),
    path('Customer/', CustomerList.as_view()),
    path('Customer/', CustomerDetail.as_view()),
    path('education_and_training/', education_and_trainingList.as_view()),
    path('education_and_training/', education_and_trainingDetail.as_view()),
    path('pst_five_work/', pst_five_workList.as_view()),
    path('pst_five_work/', pst_five_workDetail.as_view()),
    path('practise_outside/', practise_outsideList.as_view()),
    path('practise_outside/', practise_outsideDetail.as_view()),
    path('character_ref/', character_refList.as_view()),
    path('character_ref/', character_refDetail.as_view()),
    path('rivate_practice/', rivate_practiceList.as_view()),
    path('rivate_practice/', rivate_practiceDetail.as_view()),
    path('User/', UserList.as_view()),
    path('User/', UserDetail.as_view()),
      
]
