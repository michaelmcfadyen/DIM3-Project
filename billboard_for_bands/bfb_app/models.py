from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Promoter(models.Model):

class Band(models.Model)

class Venue(models.Model)

class Advert(models.Model)

class Genre(models.Model)

class UserProfile(models.Model):
        # This field is required.
        user = models.OneToOneField(User)
        # These fields are optional
        website = models.URLField(blank=True)
        picture = models.ImageField(upload_to='imgs', blank=True)

        def __unicode__(self):
                return self.user.username
class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = UserProfile
