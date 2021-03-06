# Generated by Django 2.0.6 on 2018-06-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_to_pdf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
        migrations.AddField(
            model_name='project',
            name='is_nda',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='communication',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='technicalexpertise',
            name='description',
            field=models.TextField(),
        ),
    ]
