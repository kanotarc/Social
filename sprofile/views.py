# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm as LoginForm
from django.contrib.auth import views, authenticate
from registration.forms import RegistrationFormUniqueEmail

def reg(request):
    user = User()
    user.username = request.POST.get('username','')
    user.set_password(request.POST.get('password',''))
    user.save()

def login(request):
    if request.POST:
        '''login'''
        print request.POST
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user and user.is_active:
            views.login(request)
        return redirect('/')
    else:
        form=LoginForm()
    return render(request,"social/login.html",{'form':form})

def logout(request):
    views.logout(request)
    return redirect('/')

def register(request, success_url=None,
             #form_class=RegistrationForm,
             form_class=RegistrationFormUniqueEmail,
             profile_callback=None,
             template_name='registration/registration_form.html',
             extra_context=None):
    form = form_class()
    if request.POST:
        form = form_class(data=request.POST)
        #form = RegistrationFormUniqueEmail()

        if form.is_valid():
            user = User()
            user.set_password(form.cleaned_data.get('password'))
            user.email = form.cleaned_data.get('email')
            user.username = form.cleaned_data.get('username')
            user.save()
    else:

        return render(request,template_name, {'form':form})
    return redirect('/')
