from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from bfb_app.models import UserProfile
from bfb_app.models import UserForm, UserProfileForm
from bfb_app.models import Advert,AdvertForm
from django.http import HttpResponse
from django.shortcuts import render_to_response

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

def add_advert(request):
        # immediately get the context - as it may contain posting data
        context = RequestContext(request)
        if request.method == 'POST':
                # data has been entered into the form via Post
                form = AdvertForm(request.POST)
                if form.is_valid():
                        # the form has been correctly filled in,
                        # so lets save the data to the model
                        ad = form.save(commit=True)
                        # show the index page with the list of categories
                        return index(request)
                else:
                        # the form contains errors,
                        # show the form again, with error messages
                        pass
        else:
                # a GET request was made, so we simply show a blank/empty form.
                form = AdvertForm()

        # pass on the context, and the form data.
        return render_to_response('bfb_app/add_advert.html',
                {'form': form }, context)

def register(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                uform = UserForm(data = request.POST)
                pform = UserProfileForm(data = request.POST)
                if uform.is_valid() and pform.is_valid():
                        user = uform.save()
                        # form brings back a plain text string, not an encrypted password
                        pw = user.password
                        # thus we need to use set password to encrypt the password string
                        user.set_password(pw)
                        user.save()
                        profile = pform.save(commit = False)
                        profile.user = user
                        profile.save()
                        registered = True
                else:
                        print uform.errors, pform.errors
        else:
                uform = UserForm()
                pform = UserProfileForm()

        return render_to_response('bfb_app/register.html', {'uform': uform, 'pform': pform, 'registered': registered }, context)

