# Generated by Django 3.0.4 on 2020-04-18 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20200417_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='old_author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='is_published',
            new_name='old_is_published',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='old_published',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated',
            new_name='old_updated',
        ),
    ]
