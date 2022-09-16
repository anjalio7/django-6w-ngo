from django.urls import path
from . import views

urlpatterns = [
    path('home', views.layout, name = "home"),
    path('login', views.login_view, name = "login"),
    path('addevents', views.add_events, name = "addevents"),
    path('allEvents', views.allEvents, name="allEvents"),
    path('editEvent/<int:ids>', views.editEvent, name = "edit-event"),
    path('gallery', views.gallery_view , name="gallery"),
    path('viewGallery', views.viewGallery , name="viewGallery"),
    path('deleteGallery/<int:type>', views.deleteimg , name="deleteGallery"),
    path('editGallery/<int:type>', views.editGallery , name="editGallery"),
    path('addPersons', views.addPersons, name="addPersons"),
    path('allPersons', views.allPersons, name = "allPersons"),
    path('editdetails/<int:ids>', views.editdetails, name = "editdetails"),
    path('deletedetails/<int:ids>', views.deletedetails, name="deletedetails"),
    path('logout', views.logout_view, name = 'logout'),
    path('adminDonation', views.allDonations, name='adminDonation')
]


