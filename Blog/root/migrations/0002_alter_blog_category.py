# Generated by Django 4.2 on 2023-04-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.IntegerField(choices=[(0, 'AI'), (1, 'Time'), (2, 'Psychology'), (3, 'Top')], default=0),
        ),
    ]