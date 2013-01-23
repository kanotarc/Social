# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
from sprofile.form import RegistrationForm
from django.contrib.auth.decorators import login_required
#from sprofile.models import User
from django.contrib.auth.models import User
from django.http import HttpResponse
#@login_required(login_url='/login')
from u008 import settings

def home(request):
    #return HttpResponse('<input type="text">')
    return render_to_response("social/index.html", context_instance=RequestContext(request))

def profile(request, id=None):
    if id is not None:
        user=User.objects.get(pk=id)
    else:
        user=request.user
    return render(request,'registration/profile.html',{'profile':user})

def finreg(request):
    form = RegistrationForm(instance=request.user.get_profile())

    if request.POST:
        form = RegistrationForm(instance=request.user.get_profile(),data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            resize_avatar(obj.avatar.path)
        else:

            return render(request, 'registration/finreg.html',{'form':form})
        return redirect('/accounts/profile')
    return render(request, 'registration/finreg.html',{'form':form})

def resize_avatar(path):
    from PIL import Image
    im = Image.open(path)
    im.thumbnail((150,150))
    im.save(path)
