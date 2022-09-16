from django.urls import path
from . import views

urlpatterns =[
    path('userLogin', views.login_view, name='userLogin'),
    path('userRegister', views.register, name='userRegister'),
    path('userLogout', views.logout_view, name='userLogout'),
    path('viewGallery/<int:eventId>', views.viewGallery, name='viewGallery'),
    path('', views.index, name = 'index'),
    path('donate', views.donate, name='donate'),
    path('allDonations', views.allDonations, name = 'allDonations'),
    path('personDetails', views.persons, name='personDetails'),
]
