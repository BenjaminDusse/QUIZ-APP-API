# Generated by Django 3.2.15 on 2022-09-24 20:45

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_alter_quiz_host_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='host_id',
            field=models.IntegerField(default=quiz.models.random_number, unique=True),
        ),
    ]