from django.conf.urls import patterns, url

from bfb_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^about',views.about, name='about'),
	url(r'^adv_add/$', views.add_advert, name='add_advert')
)
