# Generated by Django 3.2.15 on 2022-09-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='male_img.png', null=True, upload_to='profile_images/'),
        ),
    ]