# Generated by Django 3.0.4 on 2020-04-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20200414_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_content',
            field=models.CharField(max_length=280),
        ),
    ]