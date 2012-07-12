from django.contrib.auth.models import User

from django.forms import ModelForm

class user_profile(models.Model):
    class Meta:
        app_label = 'main'

    # This field is required.
    user = models.OneToOneField(User)

    possible_genders = (('male', 'Male',),
                         ('female', 'Female'),)

    dob    = models.DateField()
    gender = models.CharField(choices=possible_genders, max_length=6)
    
    #inches
    height = models.IntegerField()
    # lbs
    weight = models.IntegerField()
    bio    = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    

class user_profile_form(ModelForm):
    class Meta:
        model = user_profile

    
