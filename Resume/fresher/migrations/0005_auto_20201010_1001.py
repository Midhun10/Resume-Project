# Generated by Django 3.1.1 on 2020-10-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresher', '0004_delete_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='Profile_Picture',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
