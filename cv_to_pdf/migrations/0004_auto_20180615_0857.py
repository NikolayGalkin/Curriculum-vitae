# Generated by Django 2.0.6 on 2018-06-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_to_pdf', '0003_auto_20180614_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='project_title',
        ),
        migrations.AddField(
            model_name='project',
            name='nda_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='technicalexpertise',
            name='index',
            field=models.SmallIntegerField(default=0),
        ),
    ]
