# Generated by Django 3.2.15 on 2022-09-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_quiz_host_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='host_id',
            field=models.PositiveBigIntegerField(default=9710493258, unique=True),
        ),
    ]