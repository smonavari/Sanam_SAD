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
from user.forms import *


def signUp(request):
  if request.user.is_authenticated()==False:
    if request.method == 'GET':
        return render_to_response('signup.html', {'memberform': MemberModelForm(), 'userform': UserModelForm(),
                                                  'subcategories': Subcategory.objects.all(),
                                                  'category': Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        memberform = MemberModelForm(request.POST, request.FILES)
        userform = UserModelForm(request.POST)
        if userform.is_valid() & memberform.is_valid():
            print('valid')
            user = userform.save(commit=False)
            user.set_password(userform.cleaned_data["password"])

            user.save()
            member = memberform.save(commit=False)
            member.user = user
            print(user.pk)
            member.photo = request.FILES['photo']
            member.save()

            return HttpResponseRedirect("/login")
        else:
            print('not valid')
            return render_to_response('signup.html',
                                      {'userform': userform,
                                       'memberform': memberform,
                                       'subcategories': Subcategory.objects.all(),
                                       'category': Category.objects.all()},
                                      context_instance=RequestContext(request))
  else:
    return HttpResponseRedirect("/login")
