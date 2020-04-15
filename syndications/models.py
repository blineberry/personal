from django.db import models
import twitter
from django.conf import settings
import json
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Syndication():
    name = models.TextField(max_length=50)
    url = models.TextField(max_length=2000)

    @staticmethod
    def syndicate_to_twitter(content):
        api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
        response = api.PostUpdate(content)
        return response

    @staticmethod
    def delete_from_twitter(id_str):
        api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
        
        response = api.DestroyStatus(id_str)
        print(response)
        return response

    class Meta:
        abstract = True

class Tweet(models.Model):
    id_str = models.TextField(max_length=40)
    created_at = models.DateTimeField()
    screen_name = models.CharField(max_length=30)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_url(self):
        return f'https://twitter.com/{self.screen_name}/status/{self.id_str}'

    def to_syndication(self):
        return Syndication(name='Twitter',url=self.get_url())

class TwitterSyndicatable(models.Model):
    syndicated_to_twitter = models.DateTimeField(null=True)
    syndicate_to_twitter = models.BooleanField(default=False)
    tweet = GenericRelation(Tweet)
    
    def is_syndicated_to_twitter(self):
        return self.tweet.all().exists()

    def to_twitter_status(self):
        pass

    class Meta:
        abstract = True