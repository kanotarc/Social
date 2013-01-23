from django.db import models
from django.contrib.auth.models import User as sUser
# Create your models here.
from django.db.models import Q

STATUSES=(
    ('act', 'active'),
    ('follow', 'follow')
)

class FriendManager(models.Manager):

    def get_friends(self,user, list_type=0):

        if  not list_type:
            list_type = 0
        list_type = int(list_type)
        if list_type==0:#our real friends

            return self.filter(from_user=user,status="act")
        if list_type==1:#I am his follower
            return self.extra(where=['from_user_id=%d and status="%s"' % (user.id, 'follow')])
        if list_type==2:#He is my follower
            #kolvo = (self.extra(where=['to_user_id=%d and status="%s"' % (user.id, 'follow')])).count()
            return self.extra(where=['to_user_id=%d and status="%s"' % (user.id, 'follow')])





    def check_friends(self, user, friend):
        find = self.extra(where=['(from_user_id=%d and to_user_id=%d) or (from_user_id=%d and to_user_id=%d)' % (user.id, friend.id,friend.id, user.id,)])
        if find:
            if (find[0].status=='act'):
                return 1
            if (find[0].to_user == user) and (find[0].status == 'follow'):
                return 3
            if (find[0].from_user == user) and (find[0].status == 'follow'):
                return 2

        else:
            return 0

    def are_friends(self, user, friend):
        find = self.extra(where=['(from_user_id=%d and to_user_id=%d) or (from_user_id=%d and to_user_id=%d)' % (user.id, friend.id,friend.id, user.id,)])
        if find:

            if (find[0].to_user == user) and (find[0].status == 'follow'):
                self.create(from_user=find[0].to_user, to_user=find[0].from_user, status='act')
                find[0].status = 'act'
                find[0].save()
                return 0
        else:
            self.create(from_user=user, to_user=friend, status='follow')
            return 1
    def no_more_friends(self, user, friend):
        find = self.filter(Q(from_user=user, to_user_id=friend) | Q(from_user=friend, to_user=user))
        if find.count() == 2 and 'follow' not in find.values('status'):
            """
            are friends
            """

            my_friend = find.filter(to_user=friend)
            my_friend.update(status='follow')
            find.filter(status='act').delete()

            return 0
        else:
            find.filter(status='follow').delete()
            return 1
#
#            if  (find[0].status == 'follow'):
#                find[0].delete()
#            if (find[0].status == 'act'):
#                if (find[0].to_user == user):
#                    x=0
#                else:
#                    x=1
#                find[x].status='follow'
#                find[x].save()
#                find[1-x].delete()
#        return x


class Friend(models.Model):
    from_user=models.ForeignKey(sUser, related_name='+')
    to_user=models.ForeignKey(sUser, related_name='to_user_friends')
    status=models.CharField(max_length=100,
                            choices=STATUSES)
    objects = FriendManager()

    def __unicode__(self):
        return u'%s, %s' % (self.from_user.username,self.to_user.username)