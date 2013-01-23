from django.template import RequestContext
from django.template.loader import render_to_string
from django import template
register = template.Library()
from friend.models import Friend

def upper(string):
    return string.upper()
register.simple_tag(upper, name='up')

def is_friend(user,friend):
#    if type(user) == str or type(friend) == str:
#        return
    are_friends = Friend.objects.check_friends(user, friend)
    #return str(are_friends)
    return render_to_string('friends/friend_button.html', {'status':are_friends, 'profile':friend})
register.simple_tag(is_friend, name='is_friend')

def test(user,friend):
    pass


