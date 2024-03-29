# Generated by Django 3.2.11 on 2022-04-30 16:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import utils.datetime_utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('api', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='end_time',
            field=models.DateTimeField(default=utils.datetime_utils.datetime_now_plus_minutes),
        ),
        migrations.AddField(
            model_name='test',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
