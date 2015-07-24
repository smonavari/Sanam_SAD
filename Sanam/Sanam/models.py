from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Category(models.Model):
    name = models.CharField(max_length=40)
    def  __str__(self):
        return "{}".format(self.name)


class Subcategory(models.Model):
    name = models.CharField(max_length=40)
    superCategory = models.ForeignKey(Category)
    def  __str__(self):
        return "{}".format(self.name)


class Member(models.Model):
    user = models.OneToOneField(User, related_name="userProfile", unique=True)
    gender = models.BooleanField()
    photo = models.ImageField(upload_to='memberImages')
    def  __str__(self):
        return "{}".format(self.user.first_name+self.user.last_name)


class EventMaker(models.Model):
    user = models.ForeignKey(Member)
    def  __str__(self):
        return "{}".format(self.user.user.first_name+self.user.last_name)


class Buyer(models.Model):
    user = models.ForeignKey(Member)
    def  __str__(self):
        return "{}".format(self.user.user.first_name+self.user.last_name)


class Event(models.Model):
    title = models.CharField(max_length=40)
    address = models.TextField()
    subcategory = models.ForeignKey(Subcategory)
    endDate = models.DateField()
    startTime = models.DateField()
    seller = models.ForeignKey(EventMaker)
    def  __str__(self):
        return "{}".format(self.title)


class EventImage(models.Model):
    image = models.ImageField(upload_to='events')
    event = models.ForeignKey(Event)


class OrderList(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pursuitNum = models.CharField(max_length=14)
    user = models.ForeignKey(Buyer)


class TicketType(models.Model):
    event = models.ForeignKey(Event)
    price = models.IntegerField()
    location = models.TextField()
    time = models.DateTimeField(null=True)
    capacity = models.IntegerField(blank=True)


class Ticket(models.Model):
    ticketType = models.ForeignKey(TicketType)
    seatNum = models.IntegerField()
    orderList = models.ForeignKey(OrderList)


class Comment(models.Model):
    body = models.TextField(null=True)
    event = models.ForeignKey(Event)
    user = models.ForeignKey(Member)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
