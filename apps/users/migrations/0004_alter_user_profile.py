# Generated by Django 3.2.15 on 2022-09-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_email'),
        ('users', '0003_alter_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.profile'),
            preserve_default=False,
        ),
    ]