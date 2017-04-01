from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import login,base,index,profiles,logout,test
from django.conf.urls.static import static  
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_hrms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',login),
    url(r'^base/$',base),
    url(r'^index/$',index),
    url(r'^profiles/$',profiles),
    url(r'^logout/$',logout),
    url(r'^test/$',test),
)
