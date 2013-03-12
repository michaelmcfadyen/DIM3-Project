from django.conf.urls import patterns, url

from bfb_app import views

urlpatterns = patterns('',
        url(r'^$', views.anon_home, name='index'),
	url(r'^adv_add/$', views.add_advert, name='add_advert'),
	url(r'^register/$', views.register, name='register'),
	url(r'^base/$', views.base, name='base'),
	url(r'^register/promoter/$',views.registerPromoter, name='registerPromoter'),
	url(r'^register/artist/$',views.registerArtist, name='registerArtist'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^PromoterHome', views.promoterHome, name='Promoter Home'),
	url(r'^ArtistHome', views.artistHome, name='Artist Home'),
	url(r'^PromoterProfile',views.promoterProfile, name = 'Promoter Profile'),
	url(r'^ArtistProfile',views.artistProfile, name = 'Artist Profile'),
	url(r'^AdvertProfile',views.advertProfile, name = 'Advert Profile'),
	url(r'^reviewSubmissions',views.reviewSubmissions, name = 'Review Submissions'),
	url(r'^browse',views.anon_browse,name = 'Browse'),
	url(r'^artistBrowse', views.artist_browse, name = 'Artist Browse'),
	url(r'^appliedGigs',views.artist_applied_gigs, name = 'Applied Gigs'),
	url(r'^process',views.process_JSON, name = 'Process'),
	url(r'^review', views.review, name = 'Review')

)
