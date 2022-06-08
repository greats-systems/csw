from django.urls import path
# from csw import views
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('form1/', views.form1, name='form1'),
    path('work_contact/', views.work_contact, name='work_contact'),
    path('edu/', views.edu, name='edu'),
    path('pst5/', views.pst5, name='pst5'),
    path('charf/', views.charf, name='charf'),
    path('pract/', views.pract, name='pract'),
    path('priv/', views.priv, name='priv'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
