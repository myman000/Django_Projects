# Generated by Django 4.1.5 on 2023-03-02 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0013_alter_task_importance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='importance',
            new_name='priority',
        ),
    ]