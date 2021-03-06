from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',   
    url(r'^login', 'etherkeeper.core.views.login_view', name='login'),
    url(r'^logout', 'etherkeeper.core.views.logout_view', name='logout'),
    url(r'^search/users', 'etherkeeper.core.views.search_users_view', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/etherpad/create', 'etherkeeper.etherpad.views.create_view'),
    url(r'^api/etherpad/open', 'etherkeeper.etherpad.views.open_view'),
    url(r'^api/etherpad/title', 'etherkeeper.etherpad.views.title_view'),
    url(r'^api/etherpad/sharing', 'etherkeeper.etherpad.views.open_sharing_view'),
    url(r'^api/etherpad/share', 'etherkeeper.etherpad.views.share_view'),
    url(r'^api/etherpad/respond', 'etherkeeper.etherpad.views.respond_view'),
    url(r'^api/etherpad/set_title', 'etherkeeper.etherpad.views.set_title_view'),
    url(r'.*', 'etherkeeper.core.views.home_view', name='home'),
)
