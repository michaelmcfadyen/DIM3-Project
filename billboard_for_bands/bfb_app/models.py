from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=20)
	emailaddress = models.CharField(max_length=100)
	
	class Meta:
		abstract=True;

class Artist(User):
	name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
	description = models.CharField(max_length=2000)
	website = models.URLField()
	music = models.URLField()

	def _unicode_(self):
		return self.name

class Advert(models.Model):
	artist = models.ManyToManyField(Artist)
	title = models.CharField(max_length = 50)
	start_time = models.TimeField()
	duration = models.TimeField()
	date = models.DateField()
	description = models.CharField(max_length=5000)
	band = models.CharField(max_length=50)

	def __unicode__(self):
             return self.title

class Genre(models.Model):
	artist = models.ManyToManyField(Artist)
	advert = models.ManyToManyField(Advert)
	genre = models.CharField(max_length=20)

	def _unicode_(self):
		return self.genre


class Venue(models.Model):
	advert = models.ForeignKey(Advert)
	name = models.CharField(max_length=100)	
	address = models.CharField(max_length=500)
	website = models.URLField()

	def _unicode_(self):
		return self.name

class Promoter(User):
	advert = models.ForeignKey(Advert)
	name = models.CharField(max_length=50)
	phone_num = models.CharField(max_length=20)

	def __unicode__(self):
             return self.name

class AdvertForm(forms.ModelForm):
        title = forms.CharField(max_length=50,
                help_text='Please enter the title of the Event:')
	start_time = forms.TimeField(help_text='Please enter the start time of the Event:')
	duration = forms.TimeField(help_text='Please enter the duration of the slot:')
	date = forms.DateField(help_text='Please enter the date of the event:')
	description = forms.CharField(max_length=5000,help_text='Please enter a description for the event:')
	band = forms.CharField(max_length=50,help_text='Please enter the headline band for the event:')
	
        class Meta:
                # associate the model, Category, with the ModelForm
                model = Advert
		fields = ('title','start_time','duration','date','description','band')

#class UserProfile(models.Model):
#        # This field is required.
#        user = models.OneToOneField(User)
#        # These fields are optional
#        website = models.URLField(blank=True)
#        picture = models.ImageField(upload_to='imgs', blank=True)
#
#        def __unicode__(self):
#                return self.user.username
#
#class UserForm(forms.ModelForm):
#        class Meta:
#                model = User
#                fields = ["username", "email", "password"]

#class UserProfileForm(forms.ModelForm):
 #       class Meta:
  #              model = UserProfile
