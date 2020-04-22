# Generated by Django 3.0.4 on 2020-04-17 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
        ('posts', '0018_auto_20200416_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts_post_related', related_query_name='posts_posts', to='feed.Tag'),
        ),
    ]