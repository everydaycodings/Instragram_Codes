# Generated by Django 3.1 on 2020-09-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everydaycodings', '0005_auto_20200908_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='item',
            field=models.IntegerField(default=1, verbose_name='Item'),
        ),
    ]
