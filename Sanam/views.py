from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from Sanam.models import *
from Sanam.forms import *
from django.http import Http404
from django.views.generic import CreateView
from django.forms.formsets import formset_factory
from datetime import date

# Create your views here.
def mainPage(request):
    latestevent = Event.objects.all().order_by('-addtime')[:4]
    if request.user.is_authenticated():
        return if_login(request)

    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return if_login(request)

            return login(request, True)
    return render_to_response("index.html", {'subcategories': Subcategory.objects.all(),
                                             'topevents': Event.objects.all().order_by('-avgrate')[:4],
                                             'category': Category.objects.all(), 'latest': latestevent, },
                              context_instance=RequestContext(request))


def if_login(request):
    latestevent = Event.objects.all().order_by('addtime')[:4]
    return render_to_response("index.html", {'subcategories': Subcategory.objects.all(),
                                             'topevents': Event.objects.all().order_by('-avgrate')[:4],
                                             'category': Category.objects.all(), 'latest': latestevent},
                              context_instance=RequestContext(request))


def login(request, is_error=False):
    if request.user.is_authenticated():
        print(request)
        return render_to_response("UserAdmin.html",
                                  {'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                                  context_instance=RequestContext(request))

    if is_error:
        return render_to_response("header.html",
                                  {'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                                  context_instance=RequestContext(request))

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('pass', '')
        print(password)
        print(username)
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            if_login(request)
        is_error = True;

        return HttpResponseRedirect("/")
    return render_to_response("sign in.html",
                              {'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                              context_instance=RequestContext(request))


def forgot(request):
    if request.user.is_authenticated():
        return if_login(request)
    return render_to_response("forgotPassword.html")


@login_required
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


@login_required
def AddEvent(request):
    if request.method == 'GET':
        return render_to_response('AddNewEvent.html', {'formset': TicketFormSet(), 'form': EventModelForm(),
                                                       'subcategories': Subcategory.objects.all(),
                                                       'category': Category.objects.all()},
                                  context_instance=RequestContext(request))

    else:
        form = TicketFormSet(request.POST)
        eventform = EventModelForm(request.POST, request.FILES)
        if eventform.is_valid():
            eventform.save()
            for frm in form:
                frm.save()
            success = True
            return render_to_response('AddNewEvent.html', {'success': success, 'form': EventModelForm(),
                                                           'subcategories': Subcategory.objects.all(),
                                                           'category': Category.objects.all()},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('AddNewEvent.html',
                                      {'form': EventModelForm(request), 'subcategories': Subcategory.objects.all(),
                                       'category': Category.objects.all()},
                                      context_instance=RequestContext(request))


class AddEventView(CreateView):
    template_name = 'AddNewEvent.html'
    form_class = EventModelForm

    def get_context_data(self, **kwargs):
        context = super(AddEventView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = TicketFormSet(self.request.POST)
        else:
            context['formset'] = TicketFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if True:
            form = TicketFormSet(self.request.POST)
            eventform = EventModelForm(self.request.POST, self.request.FILES)
            newEvent = eventform.save(commit=False)
            newEvent.EventImage = self.request.FILES['EventImage']
            newEvent.save()
            # self.request.POST('form')
            for frm in form:
                newType = frm.save(commit=False)
                newType.event_id = newEvent.pk
                print(newEvent.pk)
                newType.save()

            print('save')
            success = True
            return render(self.request, 'AddNewEvent.html',
                          {'form': form, 'success': success, 'subcategories': Subcategory.objects.all(),
                           'category': Category.objects.all()})
        else:
            print('khar')
            return render(self.request, 'AddNewEvent.html',
                          {'form': form, 'formset': formset, 'subcategories': Subcategory.objects.all(),
                           'category': Category.objects.all()})


@login_required
def events(request):
    return render_to_response("eventlist.html",
                              {'events': Event.objects.all(), 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all()}, context_instance=RequestContext(request))


# ##EDIT
def eventsForCat(request, category_id):
    return render_to_response("Search.html",
                              {'events': Event.objects.filter(subcategory__superCategory__pk=category_id),
                               'title': Category.objects.get(pk=category_id).name,
                               'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                              context_instance=RequestContext(request))


def eventsForSubCat(request, subcategory_id):
    return render_to_response("Search.html", {'events': Event.objects.filter(subcategory__pk=subcategory_id),
                                              'title': Subcategory.objects.get(pk=subcategory_id).name,
                                              'subcategories': Subcategory.objects.all(),
                                              'category': Category.objects.all()},
                              context_instance=RequestContext(request))


@login_required
def removeEvent(request, event_id):
    Event.objects.get(pk=event_id).delete()
    return HttpResponseRedirect("/events")


@login_required
def editEvent(request, event_id):
    if request.method == 'GET':
        return render_to_response("EditEvent.html",
                                  {'form': EventModelForm(instance=Event.objects.filter(pk=event_id)[0]),
                                   'subcategories': Subcategory.objects.all(),
                                   'event':Event.objects.filter(pk=event_id)[0],
                                   'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        form = EventModelForm(request.POST, request.FILES)
        event = form.save(commit=False)
        event.pk = event_id
        event.EventImage = request.FILES['EventImage']
        # print(event)
        event.save()
        return HttpResponseRedirect("/events")
@login_required
def editTicketType(request, tick_id):
    if request.method == 'GET':
        return render_to_response("EditTicketType.html",
                                  {'form': TicketModelForm(instance=TicketType.objects.filter(pk=tick_id)[0]),
                                   'subcategories': Subcategory.objects.all(),

                                   'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        form = TicketModelForm(request.POST)
        event = form.save(commit=False)
        event.pk =tick_id
        event.event=TicketType.objects.filter(pk=tick_id)[0].event
        event.save()
        return HttpResponseRedirect("/events")

@login_required
def profile(request):
    print(request.user)
    if request.user.is_staff:
        return render_to_response("UserAdmin.html",
                                  {'Events': Event.objects.all(), 'subcategories': Subcategory.objects.all(),
                                   'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    raise Http404


@login_required
def addCategory(request):
    if request.method == 'GET':
        return render_to_response("CategoryAdd.html",
                                  {'form': CategoryModelForm(), 'subcategories': Subcategory.objects.all(),
                                   'category': Category.objects.all()}, context_instance=RequestContext(request))
    else:
        form = CategoryModelForm(request.POST, request)
        form.save()
        return render_to_response("CategoryAdd.html", {'success': True, 'form': CategoryModelForm(),
                                                       'subcategories': Subcategory.objects.all(),
                                                       'category': Category.objects.all()},
                                  context_instance=RequestContext(request))


@login_required
def addSubCategory(request):
    if request.method == 'GET':
        return render_to_response("SubCategoryAdd.html",
                                  {'form': SubCategoryModelForm(), 'subcategories': Subcategory.objects.all(),
                                   'category': Category.objects.all()}, context_instance=RequestContext(request))
    else:
        form = SubCategoryModelForm(request.POST, request)
        form.save()
        return render_to_response("SubCategoryAdd.html", {'success': True, 'form': SubCategoryModelForm(),
                                                          'subcategories': Subcategory.objects.all(),
                                                          'category': Category.objects.all()},
                                  context_instance=RequestContext(request))


@login_required
def removeCategory(request, category_id):
    Category.objects.get(pk=category_id).delete()
    return HttpResponseRedirect("/")


def category(request):
    return render_to_response("CategoryList.html",
                              {'categories': Category.objects.all(), 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all()}, context_instance=RequestContext(request))


def subcategory(request):
    return render_to_response("SubCategoryList.html",
                              {'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                              context_instance=RequestContext(request))


@login_required
def removesubCategory(request, subcategory_id):
    Subcategory.objects.get(pk=subcategory_id).delete()
    return HttpResponseRedirect("/")


@login_required
def editsubCategory(request, subcategory_id):
    if request.method == 'GET':
        return render_to_response("SubCategoryAdd.html", {
            'form': SubCategoryModelForm(instance=Subcategory.objects.filter(pk=subcategory_id)[0]),
            'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        # Subcategory.objects.get(pk=subcategory_id).delete()
        form = SubCategoryModelForm(request.POST, request)
        updatedSubcategory = form.save(commit=False)
        updatedSubcategory.pk = subcategory_id
        updatedSubcategory.save()

        return render_to_response("SubCategoryAdd.html", {'success': True, 'form': SubCategoryModelForm(
            instance=Subcategory.objects.filter(pk=subcategory_id)[0]), 'subcategories': Subcategory.objects.all(),
                                                          'category': Category.objects.all()},
                                  context_instance=RequestContext(request))


@login_required
def editCategory(request, category_id):
    if request.method == 'GET':
        return render_to_response("CategoryAdd.html",
                                  {'form': CategoryModelForm(instance=Category.objects.filter(pk=category_id)[0]),
                                   'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        form = CategoryModelForm(request.POST, request)
        editedCategory = form.save(commit=False)
        editedCategory.pk = category_id
        editedCategory.save()
        return render_to_response("CategoryAdd.html", {'success': True, 'form': CategoryModelForm(
            instance=Category.objects.filter(pk=category_id)[0]), 'subcategories': Subcategory.objects.all(),
                                                       'category': Category.objects.all()},
                                  context_instance=RequestContext(request))


def about(request):
    return render_to_response("AboutPage.html",
                              {'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                              context_instance=RequestContext(request))


def aboutLogged(request):
    return render_to_response("AboutAfterLogin.html",
                              {'subcategories': Subcategory.objects.all(), 'category': Category.objects.all()},
                              context_instance=RequestContext(request))


@login_required
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


def event(request, event_id):
    if request.method == 'GET':
        rEvent = Event.objects.filter(pk=event_id)[0]

        #filterargs = {'user': request.user.userProfile, 'event': rEvent}
        return render_to_response("EventPage.html", {'Event': rEvent,
                                                     'subcategories': Subcategory.objects.all(),
                                                     'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        rating = request.POST.get("rate", "")
        # message=request.POST.get("message","")
        rEvent = Event.objects.filter(pk=event_id)[0]
        Member = request.user.userProfile
        rates = Rate(rate=rating, event=rEvent, user=Member)

        rates.clean()
        Rata=Rate.objects.all()
        for r in Rata:
            if r.user.user.pk==request.user.pk and r.event.pk==rEvent.pk:
                return HttpResponse('شما قبلا امتیاز داده اید :|')
        rates.save()

        rEvent.numofperson=rEvent.numofperson+1
        rEvent.save()
        rEvent.avgrate=(rEvent.avgrate*(rEvent.numofperson-1)+int(rating))/rEvent.numofperson
        rEvent.save()
        return render_to_response("EventPage.html", {
            'Event':rEvent,
            'subcategories': Subcategory.objects.all(),
            'rating':rating,
            'category': Category.objects.all()
        }, context_instance=RequestContext(request))

@login_required
def ticktypesel(request, ev_id):
    event = Event.objects.get(pk=ev_id)
    return render_to_response("TypeAndNum.html",
                              {'ev': event, 'ev_id': ev_id, 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all()}, context_instance=RequestContext(request))


@login_required
def Pardakht(request, ev_id):
    tempTicket.objects.all().delete();
    event = Event.objects.get(pk=ev_id)
    if date.today() > event.endDate:
           return render_to_response("notLogged.html",{} ,context_instance=RequestContext(request))
    for field in event.ticktype.all():
        if int(request.POST[field.title]) > field.capacity:
            return render_to_response("error.html", {'remain': field.capacity, 'type': field.title ,'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all()},
                                      context_instance=RequestContext(request));
    for field in event.ticktype.all():
        y = tempTicket(cap=int(request.POST[field.title]))
        y.ticketType = field
        y.save()
    total = 0
    for field in event.ticktype.all():
        if int(request.POST[field.title]) > field.capacity:
            return render_to_response("error.html", {'remain': field.capacity,  'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(),'type': field.title},
                                      context_instance=RequestContext(request));
        x = int(request.POST[field.title]) * field.price
        total = total + x
    return render_to_response("Bank.html", {'total': total, 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(), 'ev_id': ev_id, 'form': request.POST},
                              context_instance=RequestContext(request))


def TrackingCode(request):
    global num
    username = None
    if request.user.is_authenticated():
        username = request.user.pk
    for i in Buyer.objects.all():
        if i.pk == username:
            break
    x = OrderList(pursuitNum=num)
    x.user = i;
    x.save();
    x.pursuitNum = x.pk
    x.save()
    num = num + 1;
    for tt in TicketType.objects.all():
        for ti in tt.order.all():
            tt.capacity = tt.capacity - ti.cap
            tt.soldnum = tt.soldnum + ti.cap
            tt.save()

    for field in tempTicket.objects.all():
        y = Ticket(cap=field.cap)
        y.ticketType = field.ticketType
        y.orderList = x
        y.save()
    return render_to_response("TrackingCode.html", { 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(),'orderList': x, 'tickets': tempTicket.objects.all()},
                              context_instance=RequestContext(request))


def profile(request):
    if request.user.is_staff:
        events = Event.objects.all()
        sell = {}
        nosel = {}
        allcost = {}
        for e in events:
            selled = 0
            unselled = 0
            cost = 0
            for t in e.ticktype.all():
                selled += t.soldnum
                unselled += t.capacity
                cost += t.soldnum * t.price
            sell[e] = selled
            nosel[e] = unselled
            allcost[e] = cost
        return render_to_response("c_adminprofile.html",
                                  { 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(),'events': events, 'sell': sell, 'unsell': nosel, 'cost': allcost},
                                  context_instance=RequestContext(request))

    else:
        username = None
        if request.user.is_authenticated():
            username = request.user.pk
        for i in Buyer.objects.all():
            if i.pk == username:
                break
        return render_to_response("UserProfile.html", {'user': i, 'subcategories': Subcategory.objects.all(),
                                                       'category': Category.objects.all()},
                                  context_instance=RequestContext(request))


def printpage(request, order):
    ticks = None
    for ord in OrderList.objects.all():
        if ord.pursuitNum == order:
            ticks = ord.orderlisttick.all()
    return render_to_response("print.html", { 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(),'tickets': ticks, 'orderNum': order},
                              context_instance=RequestContext(request))


def AdminProfMinsearch(request):
    events = Event.objects.all()
    sell = {}
    nosel = {}
    allcost = {}
    for e in events:
        selled = 0
        unselled = 0
        cost = 0
        for t in e.ticktype.all():
            selled += t.soldnum
            unselled += t.capacity
            cost += t.soldnum * t.price
        sell[e] = selled
        nosel[e] = unselled
        allcost[e] = cost
    return render_to_response("c_adminprofile.html",
                              { 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(),'events': events, 'sell': sell, 'unsell': nosel, 'cost': allcost},
                              context_instance=RequestContext(request))

def search(request):
    first = request.POST['first']
    last = request.POST['last']
    events = Event.objects.all().filter(startTime__gte=first, startTime__lte=last)
    sell = {}
    nosel = {}
    allcost = {}
    for e in events:
        selled = 0
        unselled = 0
        cost = 0
        for t in e.ticktype.all():
            selled += t.soldnum
            unselled += t.capacity
            cost += t.soldnum * t.price
        sell[e] = selled
        nosel[e] = unselled
        allcost[e] = cost
    return render_to_response("c_adminprofile.html",
                              { 'subcategories': Subcategory.objects.all(),
                               'category': Category.objects.all(),'events': events, 'sell': sell, 'unsell': nosel, 'cost': allcost},
                              context_instance=RequestContext(request))

