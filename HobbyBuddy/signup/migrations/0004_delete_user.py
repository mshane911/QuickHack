# Generated by Django 3.1.6 on 2021-07-17 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]