# Generated by Django 3.2.15 on 2022-09-17 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_middle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
