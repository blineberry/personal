from django.db import models

class ProfileManager(models.Manager):
    def get_owner(self):
        owners = super().filter(is_owner = True)
        if owners.exists():
            return owners[0]
            
        return None

# Create your models here.
class Profile(models.Model): 
    system_check_deprecated_details = {
        'msg': (
            'Pages.Profile has been deprecated. Support for it (except '
            'in historical migrations) will be removed'
        ),
        'hint': 'Use Profiles.Profile instead.',  # optional
        'id': 'models.pages100',  # pick a unique ID for your field.
    }

    name = models.CharField(max_length=80)
    url = models.CharField(max_length=2000)
    url_display = models.CharField(max_length=80, null=True)
    photo = models.ImageField(null=True)
    is_owner = models.BooleanField(default=False)
    short_bio = models.CharField(max_length=160, null=True)

    objects = ProfileManager()

    def __str__(self):
        return self.name

class LinkedProfile(models.Model):
    system_check_deprecated_details = {
        'msg': (
            'Pages.LinkedProfile has been deprecated. Support for it (except '
            'in historical migrations) will be removed'
        ),
        'hint': 'Use Profiles.LinkedProfile instead.',  # optional
        'id': 'models.pages200',  # pick a unique ID for your field.
    }

    name = models.CharField(max_length=80)
    url = models.CharField(max_length=2000)
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)