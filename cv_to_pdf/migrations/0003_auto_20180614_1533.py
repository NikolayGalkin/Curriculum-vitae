# Generated by Django 2.0.6 on 2018-06-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_to_pdf', '0002_auto_20180614_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='index',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='education',
            name='index',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toolandframework',
            name='index',
            field=models.SmallIntegerField(default=0),
        ),
    ]