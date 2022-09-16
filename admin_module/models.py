from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    pass

class events(models.Model):
    name = models.CharField(max_length = 50)
    EventDate = models.CharField(max_length=20)

class gallery(models.Model):
    event_id = models.OneToOneField(events, on_delete=models. CASCADE, related_name='event_id',)
    img1 = models.ImageField(upload_to = 'image/')
    img2 = models.ImageField(upload_to = 'image/')
    img3 = models.ImageField(upload_to = 'image/')
    img4 = models.ImageField(upload_to = 'image/')
    img5 = models.ImageField(upload_to = 'image/')



class details(models.Model):
    name = models.CharField(max_length = 50)
    age = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    needs = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'image/person/')

class donations(models.Model):
    person_id = models.ForeignKey(user, on_delete=models. CASCADE, related_name='person_id')
    donation_amount = models.CharField(max_length = 50)
    reason = models.CharField(max_length = 50)
    donateDate = models.DateField(auto_now_add=True)






