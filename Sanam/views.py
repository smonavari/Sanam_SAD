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


num = 127000;
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
    return render_to_response("index.html", {'subcategories': Subcategory.objects.all(),'topevents':Event.objects.all().order_by('-avgrate')[:4], 'category':Category.objects.all(),'latest':latestevent,},
                              context_instance=RequestContext(request))


def if_login(request):
    latestevent = Event.objects.all().order_by('addtime')[:4]
    return render_to_response("index.html", {'subcategories': Subcategory.objects.all(),'topevents':Event.objects.all().order_by('-avgrate')[:4], 'category':Category.objects.all(),'latest':latestevent},
                              context_instance=RequestContext(request))


def login(request, is_error=False):
    if request.user.is_authenticated():
        print(request)
        return render_to_response("UserAdmin.html", {'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()}, context_instance=RequestContext(request))

    if is_error:
        return render_to_response("header.html", {'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()}, context_instance=RequestContext(request))

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

        return render_to_response("header.html", {'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()}, context_instance=RequestContext(request))

    return render_to_response("sign in.html", {'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()}, context_instance=RequestContext(request))


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
def AddEvent( request):
    if request.method == 'GET':
        return render_to_response('AddNewEvent.html', {'formset': TicketFormSet(), 'form': EventModelForm(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},
                                  context_instance=RequestContext(request))

    else:
        form = TicketFormSet(request.POST,request)
        eventform = EventModelForm(request.POST,request)
        if eventform.is_valid():
            eventform.save()
            for frm in form:
                frm.save()
            success = True
            return render_to_response('AddNewEvent.html', {'success': success, 'form': EventModelForm(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('AddNewEvent.html', {'form': EventModelForm(request),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},
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
            form = TicketFormSet(self.request.POST,request)
            eventform = EventModelForm(self.request.POST,request)
            newEvent=eventform.save(commit=False)
            newEvent.save()
            #self.request.POST('form')
            for frm in form:
                newType=frm.save(commit=False)
                newType.event_id = newEvent.pk
                print(newEvent.pk)
                newType.save()


            print('save')
            success = True
            return render(self.request, 'AddNewEvent.html', {'form':form ,'success': success,'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()})
        else:
            print('khar')
            return render(self.request, 'AddNewEvent.html', {'form': form,'formset':formset,'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()})
@login_required
def events(request):
    return render_to_response("eventlist.html",{'events':Event.objects.all(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))

###EDIT
def eventsForCat(request,category_id):
    return render_to_response("eventlistforCat.html",{'events':Event.objects.filter(subcategory__superCategory__pk=category_id),'title':Category.objects.get(pk=category_id).name ,'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))

def eventsForSubCat(request,subcategory_id):
    return render_to_response("eventlistforCat.html",{'events':Event.objects.filter(subcategory__pk=subcategory_id),'title':Subcategory.objects.get(pk=subcategory_id).name ,'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))


@login_required
def removeEvent(request, event_id):
    Event.objects.get(pk=event_id).delete()
    return HttpResponseRedirect("/events")

@login_required
def editEvent(request,event_id):

    if request.method=='GET':
        return render_to_response("AddNewEvent.html",{'form': EventModelForm(instance=Event.objects.filter(pk=event_id)[0]), 'subcategories':Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
    else:
        form = EventModelForm(request.POST,request)
        form.save()
        Event.objects.get(pk=event_id).delete()
        return HttpResponseRedirect("/events")


@login_required
def profile(request):
    print(request.user)
    if request.user.is_staff:
        return render_to_response("UserAdmin.html", {'Events': Event.objects.all(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},
                                  context_instance=RequestContext(request))
    raise Http404

@login_required
def addCategory(request):
    if request.method=='GET':
        return render_to_response("CategoryAdd.html",{'form': CategoryModelForm(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
    else:
        form = CategoryModelForm(request.POST,request)
        form.save()
        return render_to_response("CategoryAdd.html",{'success': True, 'form': CategoryModelForm(),'subcategories': Subcategory.objects.all(),'category':Category.objects.all()},context_instance=RequestContext(request))

@login_required
def addSubCategory(request):
    if request.method=='GET':
        return render_to_response("SubCategoryAdd.html",{'form': SubCategoryModelForm(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
    else:
        form = SubCategoryModelForm(request.POST,request)
        form.save()
        return render_to_response("SubCategoryAdd.html",{'success': True, 'form': SubCategoryModelForm(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))



@login_required
def removeCategory(request, category_id):
    Category.objects.get(pk=category_id).delete()
    return HttpResponseRedirect("/")
def category(request):
    return render_to_response("CategoryList.html",{'categories':Category.objects.all(),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
def subcategory(request):
    return render_to_response("SubCategoryList.html",{'subcategories':Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
@login_required
def removesubCategory(request, subcategory_id):
    Subcategory.objects.get(pk=subcategory_id).delete()
    return HttpResponseRedirect("/")

@login_required
def editsubCategory(request,subcategory_id):

    if request.method=='GET':
        return render_to_response("SubCategoryAdd.html",{'form': SubCategoryModelForm(instance=Subcategory.objects.filter(pk=subcategory_id)[0]), 'subcategories':Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
    else:
        Subcategory.objects.get(pk=subcategory_id).delete()
        form = SubCategoryModelForm(request.POST,request)
        form.save()
        return render_to_response("SubCategoryAdd.html",{'success': True, 'form': SubCategoryModelForm(instance=Subcategory.objects.filter(pk=subcategory_id)[0]),'subcategories':Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))

@login_required
def editCategory(request,subcategory_id):
    if request.method=='GET':
        return render_to_response("CategoryAdd.html",{'form': CategoryModelForm(instance=Category.objects.filter(pk=subcategory_id)[0]),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))
    else:
        form = SubCategoryModelForm(request.POST,request)
        form.save()
        return render_to_response("CategoryAdd.html",{'success': True, 'form': CategoryModelForm(instance=Category.objects.filter(pk=subcategory_id)[0]),'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))

def about(request):
    return render_to_response("AboutPage.html",{'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))

def aboutLogged(request):
    return render_to_response("AboutAfterLogin.html",{'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))


@login_required
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


@login_required
def ticktypesel(request, ev_id):
    event = Event.objects.get(pk=ev_id)
    return render_to_response("TypeAndNum.html",{'ev':event,'ev_id':ev_id,'subcategories': Subcategory.objects.all(), 'category':Category.objects.all()},context_instance=RequestContext(request))

def Pardakht(request, ev_id):
    tempTicket.objects.all().delete();
    event = Event.objects.get(pk=ev_id)
    for field in event.ticktype.all():
        if int(request.POST[field.title]) > field.capacity:
            return render_to_response("error.html",{'remain':field.capacity,'type':field.title},context_instance=RequestContext(request));
    for field in event.ticktype.all():
        y = tempTicket(cap=int(request.POST[field.title]))
        y.ticketType_id = field.pk
        y.save()
    total = 0
    for field in event.ticktype.all():
        if int(request.POST[field.title]) > field.capacity:
            return render_to_response("error.html",{'remain':field.capacity,'type':field.title},context_instance=RequestContext(request));
        x = int(request.POST[field.title])*field.price
        total = total+x
    return render_to_response("Bank.html",{'total':total, 'ev_id':ev_id, 'form':request.POST},context_instance=RequestContext(request))

def TrackingCode(request):
    global num
    username = None
    if request.user.is_authenticated():
        username = request.user.pk
    x = OrderList(pursuitNum = num)
    x.user_id = username
    x.save();
    num = num+1;
    for tt in TicketType.objects.all():
        for ti in tt.order.all():
            tt.capacity=tt.capacity-ti.cap;
            tt.save();

    for field in tempTicket.objects.all():
        for i in range(field.cap):
            y = Ticket();
            y.ticketType = field.ticketType;
            y.orderList_id = x.pk;
            y.save();
    return render_to_response("TrackingCode.html",{'orderList':x,'tickets':tempTicket.objects.all()},context_instance=RequestContext(request))