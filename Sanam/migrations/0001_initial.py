# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('body', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('endDate', models.DateField()),
                ('startTime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to='events')),
                ('event', models.ForeignKey(to='Sanam.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventMaker',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('gender', models.BooleanField()),
                ('photo', models.ImageField(upload_to='memberImages')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='userProfile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pursuitNum', models.CharField(max_length=14)),
                ('user', models.ForeignKey(to='Sanam.Buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('superCategory', models.ForeignKey(to='Sanam.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('seatNum', models.IntegerField()),
                ('orderList', models.ForeignKey(to='Sanam.OrderList')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('price', models.IntegerField()),
                ('location', models.TextField()),
                ('time', models.DateTimeField(null=True)),
                ('capacity', models.IntegerField(blank=True)),
                ('event', models.ForeignKey(to='Sanam.Event')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticketType',
            field=models.ForeignKey(to='Sanam.TicketType'),
        ),
        migrations.AddField(
            model_name='eventmaker',
            name='user',
            field=models.ForeignKey(to='Sanam.Member'),
        ),
        migrations.AddField(
            model_name='event',
            name='seller',
            field=models.ForeignKey(to='Sanam.EventMaker'),
        ),
        migrations.AddField(
            model_name='event',
            name='subcategory',
            field=models.ForeignKey(to='Sanam.Subcategory'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='Sanam.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='Sanam.Member'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='user',
            field=models.ForeignKey(to='Sanam.Member'),
        ),
    ]
