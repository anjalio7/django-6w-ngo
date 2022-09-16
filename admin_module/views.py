from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.db.models import Sum
from .models import user, events, gallery, details, donations

# Create your views here.
def layout(request):
    eventCount = events.objects.all().count()
    personCount = details.objects.all().count()
    donationCount = donations.objects.aggregate(TOTAL  = Sum('donation_amount'))['TOTAL']
    return render(request, 'admin_module/home.html', {'eventCount': eventCount, 'personCount': personCount, 'donationCount': donationCount})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "admin_module/login.html", {
            "message": "Invalid username and/or password."
        })
        else:
                return render(request, "admin_module/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "admin_module/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "admin_module/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
        except IntegrityError:
            return render(request, "admin_module/register.html", {
                "message": "Username already taken."
            })
        return render(request, 'admin_module/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "admin_module/register.html")

def add_events(request):
    if request.method == "POST":
        name = request.POST['name']
        EventDate = request.POST['dates']
        a = events(name = name, EventDate = EventDate)
        a.save()
        return HttpResponseRedirect(reverse(allEvents))
    else:
        return render(request, "admin_module/add_events.html")

def allEvents(request):
        table = events.objects.all()
        return render(request,'admin_module/table.html', {'data':table})

def editEvent(request, ids):
    event = events.objects.get(id = ids)
    if request.method == "POST":
        event_name = request.POST['name']
        date = request.POST['dates']

        event.name = event_name
        event.EventDate = date
        event.save()
        return HttpResponseRedirect(reverse(allEvents))
    else:
        return render(request, 'admin_module/edit_events.html', {'data': event})

def gallery_view(request):
        data = events.objects.all()
        if request.method == 'POST':
            name = request.POST['event-name']
            files = request.FILES.getlist('images')
            if len(files) != 5:
                return render(request, 'admin_module/gallery.html', {'message': 'Please upload 5 images', 'data': data})
            else:
                selType = events.objects.get(id = name)
                img1 = files[0]
                img2 = files[1]
                img3 = files[2]
                img4 = files[3]
                img5 = files[4]

                a = gallery(event_id = selType, img1 = img1, img2 = img2, img3 = img3, img4 = img4, img5 = img5)
                try:
                    a.save()
                    return HttpResponseRedirect(reverse('viewGallery'))
                except:
                    return render(request, 'admin_module/gallery.html', {'data': data, 'message': 'Gallery already exists.'})


        else:
            return render(request, 'admin_module/gallery.html', {'data': data})


    
def viewGallery(request):
    data = gallery.objects.all()
    return render(request, 'admin_module/viewGallery.html', {'data':data})

def deleteimg(request, type):
    port = gallery.objects.get(id = type)
    port.delete()
    return HttpResponseRedirect(reverse('viewGallery'))

def editGallery(request, type):
    gal = gallery.objects.get(id = type)
    data = events.objects.all()
    # print(port.photography_id//.id)
    if request.method == 'POST':
        name = request.POST['event-name']
        files = request.FILES.getlist('images')
        # files = request.FILES.getlist('img1')
        selType = events.objects.get(id = name)
        d = {}
        for i in range(len(files)):
            exec(f'gal.img{i+1} = files[i]')
        gal.event_id = selType
        try:
            gal.save()
            return HttpResponseRedirect(reverse('viewGallery'))
        except:
            return render(request, 'admin_module/editGallery.html', {'gal': gal, 'data': data, 'message': 'Gallery already exists.'})
    else:
        return render(request, 'admin_module/editGallery.html', {'gal': gal, 'data': data})

def addPersons(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        need = request.POST['needs']
        img = request.FILES['images']
        print
        a = details(name = name, age = age, gender = gender, needs = need, img = img)
        a.save()
        return HttpResponseRedirect(reverse(addPersons))
    else:
        return render(request, "admin_module/addPersons.html")


def allPersons(request):
    data = details.objects.all()
    return render(request,'admin_module/allPersons.html' , {'data':data})

def editdetails(request, ids):
    data = details.objects.get(id = ids)
    if request.method == "POST":
        print(request.POST)
        person_name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        need = request.POST['needs']
        img = request.FILES.get('images')

        if img is not None:
            data.img = img

        data.name = person_name
        data.age = age
        data.gender = gender
        data.needs = need
        data.save()
        return HttpResponseRedirect(reverse(allPersons))
    else:
        return render(request, 'admin_module/edit_details.html', {'data': data})

def deletedetails(request, ids):
    detail = details.objects.get(id = ids)
    if request.method == 'POST':
        detail.delete()
        return HttpResponseRedirect(reverse('allPersons'))
    else:
        return HttpResponseRedirect(reverse('allPersons'))

def allDonations(request):
    data = donations.objects.all()
    return render(request, 'admin_module/allDonations.html', {'data': data})


