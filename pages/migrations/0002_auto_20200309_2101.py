# Generated by Django 3.0.4 on 2020-03-09 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('url', models.CharField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='person',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='urlDisplay',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='linkedprofile',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Profile'),
        ),
    ]