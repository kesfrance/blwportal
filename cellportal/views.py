from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from cellportal.forms import UserForm, UserProfileForm
from django.views.generic import View
# Create your views here.
def dashboard(request):
    """
    Open dashboard of user.
    """
    return render(request, "cells_home.html", {})

class UserLogin(View):
    """
    Login user and redirect appropriately
    """
    def get(self, request):
        form = UserForm()
        return render(request, 'login.html', {'form':form})
    
    def post(self, request):
        form = UserForm(request.POST)
      
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/cells/")
            else:
                return HttpResponse("Your account has been disabled")
        else:
            form.errorsmsg = "Invalid login details supplied"
        return render(request, 'login.html', {'form':form})
    
def user_signup(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
            
            registered = True
        
        else:
            print(profile_form.errors) # user_form.errors, 
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request,
            'signup.html',
            {'user_form':user_form, 'profile_form':profile_form,
             'registered' : registered})


