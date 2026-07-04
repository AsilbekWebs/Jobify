from django.urls import path
from .views import *
urlpatterns = [
    path('create/', create_vacancy, name='create_vacancy'),
    path('<int:pk>/', vacancy_detail, name='vacancy_detail'),
    path('list/', vacancy_list, name='vacancy_list'),
]