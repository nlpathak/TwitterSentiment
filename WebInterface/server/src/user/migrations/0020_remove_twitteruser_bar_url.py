# Generated by Django 3.1.7 on 2021-03-03 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20210302_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitteruser',
            name='bar_url',
        ),
    ]