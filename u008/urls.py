from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from settings import APP_DIR, STATIC_ROOT, MEDIA_ROOT
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'social.views.home', name='home'),
    url('', include('registration.backends.default.urls')),
    url(r'^accounts/profile/$','social.views.profile', name='sprofile'),
    url(r'^accounts/profile/(?P<id>\d+)$','social.views.profile', name='sprofile'),
    url(r'^finreg/$','social.views.finreg',name='sprofile'),
#    url(r'^accounts/', include('registration.backends.default.urls')),
#    url(r'^register/', 'sprofile.views.register'),
    # url(r'^u008/', include('u008.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^friends/(?P<list_type>\d*)','friend.views.friends',name='friend'),
    url(r'^friend/add/(?P<friend_id>\d+)', 'friend.views.add_to_friend_list', name='add_to_friend'),
    url(r'^friend/del/(?P<friend_id>\d+)', 'friend.views.del_from_friend', name='del_from_friend'),
    url(r'^login/', 'sprofile.views.login',name='login'),
    url(r'^logout/', 'sprofile.views.logout',name='logout'),

    url(r'^search-form/$', 'friend.views.search_form', name='ser_form'),
    url(r'^search/$', 'friend.views.search', name='search'),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': APP_DIR + STATIC_ROOT}),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': APP_DIR + MEDIA_ROOT}),
)
