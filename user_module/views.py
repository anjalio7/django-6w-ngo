from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from admin_module.models import *
# Create your views here.

def index(request):
    return render(request, 'user_module/home.html')

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
                return render(request, "user_module/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "user_module/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('userLogin'))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "user_module/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
        except IntegrityError:
            return render(request, "user_module/register.html", {
                "message": "Username already taken."
            })
        return render(request, 'user_module/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "user_module/register.html")


def viewGallery(request, eventId):
    data = gallery.objects.get(event_id = eventId)
    return render(request, 'user_module/viewGallery.html', {'data': data})

def allDonations(request):
    data = donations.objects.filter(person_id = request.user)
    return render(request, 'user_module/allDonations.html', {'data': data})

def donate(request):
    if request.method == 'POST':
        amt = request.POST['amt']
        msg = request.POST.get('msg')
        a = donations(person_id = request.user, donation_amount = amt, reason = msg)
        a.save()
        return HttpResponseRedirect(reverse('allDonations'))
    else:
        return render(request, 'user_module/donate.html')

def persons(request):
    data = details.objects.all()
    return render(request, 'user_module/persons.html', {'data': data})