from django.shortcuts import render_to_response, render

from django.core.context_processors import csrf

from forms import signup_form, login_form

from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from apps.main.models.user_profile import *

def index(request):
    return render_to_response("base.djhtml", {}, context_instance=RequestContext(request))

def signup(request):
    if request.method == "POST":
        form = signup_form(request.POST)

        if form.is_valid():
            from django.contrib.auth.models import User

            new_user = User.objects.create_user(request.POST["email_address"], request.POST["email_address"], request.POST["password"])
            new_user.save()

            request.session["message"] = "Thanks for signing up with Smack, you'll receive a confirmation email shortly."

            return HttpResponseRedirect('/')
    else:
        form = signup_form()

    return render(request, "signup.djhtml", { "form": form })

def login_view(request):
    if request.method == "POST":
        form = login_form(request.POST)

        if form.is_valid():
            #import pdb;pdb.set_trace()
            user = authenticate(username=request.POST["email_address"], password=request.POST["password"])
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:                
                    pass
            else:
                # invalid login
                pass
    else:
        form = login_form()

    return render(request, "login.djhtml", { "form": form })

def logout_view(request):
    logout(request)
    
    return HttpResponseRedirect("/")

@login_required(login_url="/login")
def edit_profile(request):
    try:
        user_profile_instance = user_profile.objects.get(user=request.user)

        form = user_profile_form(instance=user_profile_instance)
    except user_profile.DoesNotExist:
        form = user_profile_form()

    if request.method == "POST":
        form.save()
    else:        
        pass

    return render(request, "edit_profile.djhtml", { "form": form })
