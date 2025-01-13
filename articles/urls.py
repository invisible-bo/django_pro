from django.urls import path
from . import views

urlpatterns = [  
    path('hello/', views.hello),
    path('data_throw/', views.data_throw),
    path('data_catch/', views.data_catch),
]