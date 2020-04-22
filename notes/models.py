from django.db import models
from profiles.models import Profile
from feed.models import Tag, FeedItem
from syndications.models import TwitterSyndicatable
from django.urls import reverse

# Create your models here.
class Note(TwitterSyndicatable, FeedItem):
    content = models.CharField(max_length=560)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('notes:detail', args=[self.id])

    def feed_item_content(self):
        return self.content

    def feed_item_header(self):
        return self.published

    def to_twitter_status(self):
        return self.content