# Generated by Django 3.2.15 on 2022-09-20 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answers', 'verbose_name_plural': 'Answer'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Questions', 'verbose_name_plural': 'Question'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Quizzes', 'verbose_name_plural': 'Quiz'},
        ),
        migrations.AlterModelOptions(
            name='quizmeta',
            options={'verbose_name': 'Quiz Metas', 'verbose_name_plural': 'Quiz Meta'},
        ),
        migrations.AlterModelOptions(
            name='quiztake',
            options={'verbose_name': 'QuizTakes', 'verbose_name_plural': 'QuizTake'},
        ),
        migrations.AlterModelOptions(
            name='takeanswer',
            options={'verbose_name': 'TakeAnswers', 'verbose_name_plural': 'TakeAnswer'},
        ),
    ]
