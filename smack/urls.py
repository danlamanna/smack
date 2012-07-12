from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smack.views.home', name='home'),
    # url(r'^smack/', include('smack.foo.urls')),    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('apps.main.views',
                        url(r'^$', 'index'),
                        url(r'^signup$', 'signup'),
                        url(r'^login$', 'login_view'),
                        url(r'^logout$', 'logout_view'),
                        url(r'^edit-profile$', 'edit_profile'),
)
