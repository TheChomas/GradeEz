# Generated by Django 3.2.11 on 2022-04-30 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220430_1707'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]