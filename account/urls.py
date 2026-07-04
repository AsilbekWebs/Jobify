from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('register/candidate/', register_candidate,  name='register_candidate'),
    path('register/company/', register_company, name='register_company'),
    path('dashboard/', dashboard, name='dashboard'),
    path('resume/create/', create_resume, name='create_resume'),

    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
