# Generated by Django 4.1.5 on 2023-03-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_remove_task_dateandtimetocompleteparticulartask_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default='date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.CharField(default='c', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(default='time'),
        ),
    ]
