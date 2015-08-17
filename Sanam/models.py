from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Subcategory(models.Model):
    name = models.CharField(max_length=40)
    superCategory = models.ForeignKey(Category, related_name='subcategories')

    def __str__(self):
        return "{}".format(self.name)


class Member(models.Model):
    user = models.OneToOneField(User, related_name="userProfile", unique=True)
    gender = models.BooleanField()
    photo = models.ImageField(upload_to='memberImages')

    def __str__(self):
        return "{}".format(self.user.first_name + self.user.last_name)


class EventMaker(models.Model):
    user = models.ForeignKey(Member)

    def __str__(self):
        return "{}".format(self.user.user.first_name + self.user.user.last_name)


class Buyer(models.Model):
    user = models.ForeignKey(Member)

    def __str__(self):
        return "{}".format(self.user.user.first_name)


class Event(models.Model):
    title = models.CharField(max_length=40)
    address = models.TextField()
    subcategory = models.ForeignKey(Subcategory,related_name='eventsubcategories')
    endDate = models.DateField()
    startTime = models.DateField()
    seller = models.ForeignKey(EventMaker, null=True)
    dscp = models.TextField(null=True)
    EventImage = models.ImageField(upload_to='events', null=True)
    avgrate = models.IntegerField(default=5)
    numofperson = models.IntegerField(default=0)
    addtime = models.DateField(null=True)

    def __str__(self):
        return "{}".format(self.title)


class OrderList(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pursuitNum = models.CharField(max_length=14)
    user = models.ForeignKey(Buyer, related_name="buyer")

class TicketType(models.Model):
    title = models.CharField(max_length=40, null=True)
    event = models.ForeignKey(Event, related_name="ticktype")
    price = models.IntegerField()
    location = models.TextField()
    time = models.DateTimeField(null=True)
    capacity = models.IntegerField(default=0)

class Ticket(models.Model):
    ticketType = models.ForeignKey(TicketType)
    orderList = models.ForeignKey(OrderList, related_name="orderlisttick")
    cap = models.IntegerField(default=0)


class tempTicket(models.Model):
    ticketType = models.ForeignKey(TicketType, related_name="order")
    cap = models.IntegerField(default=0)

class Comment(models.Model):
    body = models.TextField(null=True)
    event = models.ForeignKey(Event)
    user = models.ForeignKey(Member)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
