from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class user_profile(models.Model):
    class Meta:
        app_label = 'main'
    
    user = models.OneToOneField(User)

    possible_genders = (('male', 'Male',),
                         ('female', 'Female'),)

    dob    = models.DateField()
    gender = models.CharField(choices=possible_genders, max_length=6)
    
    #inches
    height = models.IntegerField()
    # lbs
    
    weight = models.IntegerField()
    bio    = models.CharField(max_length=255, help_text="Public")
    occupation = models.CharField(max_length=255, help_text="Public")
    

class user_profile_form(ModelForm):
    class Meta:
        model = user_profile
        exclude = ("user",)
