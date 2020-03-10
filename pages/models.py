from django.db import models

class ProfileManager(models.Manager):
    def get_owner(self):
        owners = super().filter(is_owner = True)
        if owners.exists():
            return owners[0]
            
        return None

# Create your models here.
class Profile(models.Model): 
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=2000)
    url_display = models.CharField(max_length=80, null=True)
    photo = models.ImageField(null=True)
    is_owner = models.BooleanField(default=False)

    objects = ProfileManager()

    def __str__(self):
        return self.name

class LinkedProfile(models.Model):
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=2000)
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)