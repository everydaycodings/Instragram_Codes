# Generated by Django 3.1 on 2020-09-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everydaycodings', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
