# Generated by Django 3.0.4 on 2020-05-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
