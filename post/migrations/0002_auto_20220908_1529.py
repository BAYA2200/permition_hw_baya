# Generated by Django 3.2 on 2022-09-08 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='text',
        ),
    ]