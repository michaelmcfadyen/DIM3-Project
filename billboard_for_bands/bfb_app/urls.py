from django.conf.urls import patterns, url

from bfb_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^about/$',views.about, name='about'),
	url(r'^adv_add/$', views.add_advert, name='add_advert'),
	url(r'^register/$', views.register, name='register'),
	url(r'^base/$', views.base, name='base'),
	url(r'^register/promoter/$',views.registerPromoter, name='registerPromoter'),
	url(r'^register/artist/$',views.registerArtist, name='registerArtist'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout')

)
