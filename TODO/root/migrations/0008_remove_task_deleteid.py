# Generated by Django 4.1.5 on 2023-03-02 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_alter_task_dateandtimetocompleteparticulartask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deleteID',
        ),
    ]
