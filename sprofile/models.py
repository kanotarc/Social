from django.db import models
from django.contrib.auth.models import User as sUser
from django.utils.translation import ugettext as _
import datetime
GENDER_CHOICES=(('m',_('Male')),
                ('f',_('Female')))
# Create your models here.
class User(models.Model):
    user=models.ForeignKey(sUser,unique=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=100)
    email=models.EmailField()
    birthday=models.DateField(blank=True, null=True, default=datetime.date.today())
    phone=models.CharField(max_length=100,blank=True)
    avatar=models.ImageField(upload_to='avatar', blank=True, null=True)
    def __unicode__(self):
        return ''.join(self.last_name)


def create_profile(sender, instance, created=True, **kwargs):
    if created:
        profile = User()
        profile.user = instance
        profile.save()

models.signals.post_save.connect(create_profile, sender=sUser)
