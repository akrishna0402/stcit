# Generated by Django 3.2.9 on 2021-12-31 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cit2020', '0011_auto_20201206_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slot',
            field=models.IntegerField(default=0),
        ),
    ]