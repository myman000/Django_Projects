# Generated by Django 4.1.5 on 2023-03-02 19:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0008_remove_task_deleteid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='dateAndTimeToCompleteParticularTask',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
