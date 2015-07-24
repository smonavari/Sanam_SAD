from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect, request
from django.shortcuts import render_to_response
from django.template import Template,Context , RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def mainPage(request):
    if request.user.is_authenticated():
        return if_login(request)

    else :
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return if_login(request)

            return login(request,True)

    return render_to_response("c_adminprofile.html",context_instance=RequestContext(request))

def if_login(request):
 return render_to_response("index.html")

def login(request,is_error=False):
     if request.user.is_authenticated():
        print(request)
        return render_to_response("c_adminprofile.html", {}, context_instance=RequestContext(request))

     if is_error:
        return render_to_response("header.html", {}, context_instance=RequestContext(request))

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

            return render_to_response("header.html",{} , context_instance=RequestContext(request))

     return render_to_response("sign in.html" ,{} , context_instance=RequestContext(request))

def forgot(request):
    if request.user.is_authenticated():
        return if_login(request)
    return render_to_response("forgotPassword.html")

@login_required
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


def profile(request):
    return render_to_response("c_adminprofile.html",{} , context_instance=RequestContext(request))
