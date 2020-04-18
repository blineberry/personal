# Generated by Django 3.0.4 on 2020-04-18 01:36

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_feeditem'),
        ('notes', '0003_auto_20200416_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='feeditem',
            field=models.OneToOneField(auto_created=True, db_column='feeditem_ptr', null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='note', to='feed.FeedItem'),
        ),
    ]
