"""SanamS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import os
from django.views.generic import RedirectView
from Sanam.views import AddEventView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Sanam.views.mainPage'),
    url(r'^index/', include(admin.site.urls)),
    url(r'^event/', include(admin.site.urls)),
    url(r'^profile/', 'Sanam.views.profile'),
    url(r'^bag/', include(admin.site.urls)),
    url(r'^buy/', include(admin.site.urls)),
    url(r'^login/$', 'Sanam.views.login'),

    url(r'^events/add$', AddEventView.as_view()),
    url(r'^events/$', 'Sanam.views.events'),
    url(r'^events/remove/(?P<event_id>[\d]+)$', 'Sanam.views.removeEvent'),
    url(r'^events/edit/(?P<event_id>[\d]+)$','Sanam.views.editEvent'),

    url(r'^category/add$', 'Sanam.views.addCategory'),
    url(r'^category/remove/(?P<category_id>[\d]+)$', 'Sanam.views.removeCategory'),
    url(r'^category$', 'Sanam.views.category'),
    url(r'^category/events/(?P<category_id>[\d]+)$', 'Sanam.views.eventsForCat'),
    url(r'^subcategory/events/(?P<subcategory_id>[\d]+)$', 'Sanam.views.eventsForSubCat'),


    url(r'^category/edit/(?P<subcategory_id>[\d]+)$', 'Sanam.views.editCategory'),
    url(r'^subcategory/add$', 'Sanam.views.addSubCategory'),
    url(r'^subcategory/remove/(?P<subcategory_id>[\d]+)$', 'Sanam.views.removesubCategory'),
    url(r'^subcategory/edit/(?P<subcategory_id>[\d]+)$', 'Sanam.views.editsubCategory'),
    url(r'^subcategory$', 'Sanam.views.subcategory'),

    url(r'^AboutPage.html$', 'Sanam.views.about'),
    url(r'AboutAfterLogin.html$', 'Sanam.views.aboutLogged'),
    url(r'^logout/$', 'Sanam.views.logout'),




    url(r'^ticktypesel/(?P<ev_id>[\d]+)$', 'Sanam.views.ticktypesel'),
    url(r'^Pardakht/(?P<ev_id>[\d]+)$', 'Sanam.views.Pardakht'),
    url(r'^TrackingCodeShow$', 'Sanam.views.TrackingCode'),
    url(r'^print/(?P<order>[\d]+)$', 'Sanam.views.printpage'),
    url(r'^UserProfile$', 'Sanam.views.profile'),
    url(r'^adminProfile', 'Sanam.views.AdminProfMinsearch'),
    url(r'^adminsearch','Sanam.views.search')
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root': os.path.join(BASE_DIR, 'static')})
]