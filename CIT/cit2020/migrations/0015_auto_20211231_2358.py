# Generated by Django 3.2.9 on 2021-12-31 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cit2020', '0014_auto_20211231_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot1',
            name='user',
        ),
        migrations.RemoveField(
            model_name='slot2',
            name='user',
        ),
        migrations.RemoveField(
            model_name='slot3',
            name='user',
        ),
    ]