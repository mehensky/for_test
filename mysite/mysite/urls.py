from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import here,math
from restaurants.views import menu,welcome,restaurant_list

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$',here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$',math),
    url(r'^menu/(\d{1,5})/$',menu), 		
    url(r'^welcome/$',welcome),
    url(r'^restaurant_list/$',restaurant_list),
 #   url(r'^comment/(\d{1,5})/$',comment),
)
