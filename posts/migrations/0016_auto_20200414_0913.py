# Generated by Django 3.0.4 on 2020-04-14 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_delete_twittersyndication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='long_content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='summary',
            new_name='short_content',
        ),
    ]
