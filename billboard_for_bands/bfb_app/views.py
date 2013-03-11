from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from bfb_app.models import PromoterForm, UserProfileForm, ArtistForm,Promoter, Artist
from bfb_app.models import Advert,AdvertForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

def base(request):
	template = loader.get_template('bfb_app/base.html')
	context = RequestContext(request,{}) 
	return HttpResponse(template.render(context))

def register(request):
	template = loader.get_template('bfb_app/register.html')
	context = RequestContext(request,{}) 
	return HttpResponse(template.render(context))

def anon_browse(request):
	if(request.user.is_authenticated() == False):
		ad_list = Advert.objects.all()
		template = loader.get_template('bfb_app/browse')
		context = RequestContext(request, {'ad_list':ad_list})
		return HttpResponse(template.render(context))

def advertProfile(request):
	context = RequestContext(request)
	if request.method == 'POST'and request.user.is_authenticated():
		advert_title = request.POST['']
		advert = Advert.object.filter(title=advert_title)[0]
		if(advert.count == 1):
			template = loader.get_template('bfb_app/advertProfile')
			context = RequestContext(request,{'advert' : advert})
			return HttpResponse(template.render(context))

def artistProfile(request):
	if(Artist.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated()):
		profile = Artist.objects.filter(username=request.user.username)[0]
		print profile
		template = loader.get_template('bfb_app/artistProfile.html')
		context = RequestContext(request,{profile})
		return HttpResponse(template.render(context))
	else:
		template = loader.get_template('bfb_app/index.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))
		

def promoterProfile(request):
	if(Promoter.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated()):
		profile = Promoter.objects.filter(username=request.user.username)[0]
		print profile
		template = loader.get_template('bfb_app/promoterProfile.html')
		context = RequestContext(request,{profile})
		return HttpResponse(template.render(context))
	else:
		template = loader.get_template('bfb_app/index.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))

def promoterHome(request):
	if(Promoter.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated()):
		ad_list = Advert.objects.filter(promoter = Promoter.objects.filter(username=request.user.username))
		print ad_list
		count_list = []
		for x in ad_list:
			count_list.append(x.artist.count)
		template = loader.get_template('bfb_app/promoterHome.html')
		context = RequestContext(request,{'ad_list':ad_list, 'count_list':count_list}) 
		return HttpResponse(template.render(context))
	elif Artist.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated():
		template = loader.get_template('bfb_app/artistHome.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))
	else:
		template = loader.get_template('bfb_app/index.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))
			

def artistHome(request):
	context = RequestContext(request)
	if request.method == 'GET':
		if(Artist.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated()):
			ad_list = Advert.objects.all()
			template = loader.get_template('bfb_app/artistHome.html')
			context = RequestContext(request,{'ad_list':ad_list}) 
			return HttpResponse(template.render(context))
		template = loader.get_template('bfb_app/index.html')
		context =  RequestContext(request,{})
		return HttpResponse(template.render(context))
	elif request.method == 'POST' and request.user.is_authenticated():
		advert_title = request.POST['']
		date = request.POST['']
		advert = Advert.objects.filter(title=advert_title)
		if(advert.count > 0):
			for ad in advert:
				ad.artist = Artist.filter.object(username=request.user.username);
		else:
			print 'advert does not exist'
			return render_to_response('bfb_app/artistHome.html',{},context)
	elif Promoter.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated():	
		template = loader.get_template('bfb_app/promoterHome.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))
	else:
		template = loader.get_template('bfb_app/index.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))

#def artist_applies(request):
##	
#	if (request.method == 'POST' and request.user.is_authenticated()):
#		advert_title = request.POST['']
#		date = request.POST['']
#		advert = Advert.objects.filter(title=advert_title and date=d and status=OPEN)
#		if(advert.count > 0):
#			for ad in advert:
#				ad.artist = request.user.username;
#		else:
#			print 'advert does not exist'
#			return render_to_response('',{},context)
#	else:
#		return render_to_response('',{},context)

def index(request):
        # select the appropriate template to use
        template = loader.get_template('bfb_app/index.html')
        # create and define the context. We don't have any context at the moment
        # but later on we will be putting data in the context which the template engine
        # will use when it renders the template into a page.
	ad_list = Advert.objects.all()
        context = RequestContext(request, {'ad_list':ad_list})
        # render the template using the provided context and return as http response.
        return HttpResponse(template.render(context))

def about(request):
	template = loader.get_template('bfb_app/about.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def search(request):
	context = RequestContext(request)

def add_advert(request):
	if(Promoter.objects.filter(username=request.user.username).count() > 0 and request.user.is_authenticated()):
        	# immediately get the context - as it may contain posting data
        	context = RequestContext(request)
        	if request.method == 'POST':
                	# data has been entered into the form via Post
                	form = AdvertForm(request.POST)
                	if form.is_valid():
                	        # the form has been correctly filled in,
                	        # so lets save the data to the model
                	        ad = form.save(commit=False)
	
				ad.promoter = Promoter.objects.filter(username=request.user.username)[0]
				ad.status = 'OP'
				ad.save()
                	        # show the index page with the list of categories
                	        return promoterHome(request)
               		else:
                        	# the form contains errors,
                        	# show the form again, with error messages
                        	print form.errors
        	else:
                	# a GET request was made, so we simply show a blank/empty form.
                	form = AdvertForm()

       	 	# pass on the context, and the form data.
        	return render_to_response('bfb_app/add_advert.html', {'form': form }, context)
	else:
		template = loader.get_template('bfb_app/index.html')
		context = RequestContext(request,{}) 
		return HttpResponse(template.render(context))

def registerPromoter(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                uform = PromoterForm(data = request.POST)
                #pform = UserProfileForm(data = request.POST)
                if uform.is_valid():
                        user = uform.save()
                        # form brings back a plain text string, not an encrypted password
                        pw = user.password
                        # thus we need to use set password to encrypt the password string
                        user.set_password(pw)
                        user.save()
                        #profile = pform.save(commit = False)
                        #profile.user = user
                        #profile.save()
                        #save_file(request.FILES['picture'])
                        registered = True
                else:
                        print uform.errors
        else:
                uform = PromoterForm()
               # pform = UserProfileForm()

        return render_to_response('bfb_app/registerpromoter.html', {'uform': uform, 'registered': registered }, context)

def registerArtist(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                uform = ArtistForm(data = request.POST)
               # pform = UserProfileForm(data = request.POST)
                if uform.is_valid():
                        user = uform.save()
                        # form brings back a plain text string, not an encrypted password
                        pw = user.password
                        # thus we need to use set password to encrypt the password string
                        user.set_password(pw)
                        user.save()
                        #profile = pform.save(commit = False)
                        #profile.user = user
                        #profile.save()
                        #save_file(request.FILES['picture'])
                        registered = True
                else:
			print "Form is wrong"
                        print uform.errors
        else:
                uform = ArtistForm()
               # pform = UserProfileForm()

        return render_to_response('bfb_app/registerartist.html', {'uform': uform, 'registered': registered }, context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          uname = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=uname, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
		  if(Promoter.objects.filter(username=uname).count() > 0):
			return HttpResponseRedirect("/bfb_app/PromoterHome")
		  elif Artist.objects.filter(username=uname).count() > 0:
			print "artist"
			return HttpResponseRedirect("/bfb_app/ArtistHome")
		  else:
			return HttpResponseRedirect('bfb_app/index.html')
                  return HttpResponseRedirect("/bfb_app/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  "invalid login details " + uname + " " + password
              return render_to_response('bfb_app/login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('bfb_app/login.html', {}, context)

@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/bfb_app/')


