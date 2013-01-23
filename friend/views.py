# coding:utf-8
from logging import CRITICAL
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from friend.models import Friend
from django.contrib.auth.models import User

def friends(request, list_type=0):#My friends
    friend_list = Friend.objects.get_friends(request.user, list_type)

#    if list_type == 2:
#        pass

    print friend_list
    return render(request, 'friends/list.html', {'friends':friend_list, 'list_type':int(list_type)})



def add_to_friend_list(request, friend_id):
    #messages.add_message(request, messages.INFO, "Заявка успешно обработана")
    x = Friend.objects.are_friends(request.user, User.objects.get(pk=friend_id))
    if x == 0:
        messages.add_message(request, messages.INFO, "Теперь Вы друзья")
    elif x == 1:
        messages.add_message(request, messages.INFO, "Заявка успешно подана")
    return redirect(reverse('sprofile', kwargs={'id':friend_id}))


def del_from_friend(request, friend_id):
    #messages.add_message(request, messages.INFO, "Заявка успешно обработана")
    x = Friend.objects.no_more_friends(request.user, User.objects.get(pk=friend_id))
    if x == 0:
        messages.add_message(request, messages.INFO, "Вы больше не друзья")
    elif x == 1:
        messages.add_message(request, messages.INFO, "Заявка удалена")
    return redirect(reverse('sprofile', kwargs={'id':friend_id}))





def search_form(request):
    return render(request, 'friends/search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'Вы искали: %r' % request.GET['q']
    else:

        Friend.objects.filter(name__icontains="q")
        message = 'БЛа бла'
    return HttpResponse(message)