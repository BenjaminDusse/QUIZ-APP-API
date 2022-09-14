# Generated by Django 3.2.15 on 2022-09-14 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
                ('phone', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.", regex='^998[0-9]{9}$')])),
                ('photo', models.ImageField(blank=True, null=True, upload_to='contacts/')),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]