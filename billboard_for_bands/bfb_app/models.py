from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

# Create your models here.

class Genre(models.Model):
	genre = models.CharField(max_length=20)

	def __unicode__(self):
		return self.genre

class Venue(models.Model):
	name = models.CharField(max_length=100)	
	address = models.CharField(max_length=500)
	website = models.URLField()

	def __unicode__(self):
		return self.name

class Artist(User):
	genre = models.ForeignKey(Genre)
	name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
	description = models.CharField(max_length=2000)
	website = models.URLField(blank=True)
	music = models.URLField(blank=True)

	def __unicode__(self):
		return self.name
class Promoter(User):
	name = models.CharField(max_length=50)
	phone_num = models.CharField(max_length=20)

	def __unicode__(self):
             return self.name

class Advert(models.Model):
	genre = models.ForeignKey(Genre)
	promoter=models.ForeignKey(Promoter,null=True,blank=True)
	venue=models.ForeignKey(Venue)
	artist= models.ManyToManyField(Artist,blank=True)
	title = models.CharField(max_length = 50)
	start_time = models.TimeField()
	duration = models.TimeField()
	date = models.DateField()
	description = models.CharField(max_length=5000)
	band = models.CharField(max_length=50)
	OPEN = 'OP'
	CLOSED = 'CL'
	CHOSEN = 'CH'
	status_choices = ((OPEN,'open'), (CLOSED,'closed'), (CHOSEN, 'chosen'),)
	status = models.CharField(max_length = 2, choices=status_choices,default=OPEN)

	def __unicode__(self):
             return self.title

class AdvertForm(forms.ModelForm):
	title = forms.CharField(max_length=50)
	start_time = forms.TimeField()
	duration = forms.TimeField()
	date = forms.DateField()
	description = forms.CharField(max_length=5000)
	band = forms.CharField(max_length=50)
        class Meta:
                model = Advert
		fields = ('title','start_time','duration','date','description','band', "genre", "venue")

class UserProfile(models.Model):
        # This field is required.
        user = models.OneToOneField(User)
        # These fields are optional
        website = models.URLField(blank=True)
        #picture = models.ImageField(upload_to='imgs', blank=True)

        def __unicode__(self):
                return self.user.username

class PromoterForm(forms.ModelForm):
        class Meta:
                model = Promoter
                fields = ["username", "email", "password","name","phone_num"]
class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ["username","email","password","name","phone_number","description","website","music","genre"]

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = UserProfile

