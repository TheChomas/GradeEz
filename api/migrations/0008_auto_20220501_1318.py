# Generated by Django 3.2.11 on 2022-05-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20220501_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='parent_passage',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='passage',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Passage',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
