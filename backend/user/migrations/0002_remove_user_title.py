# Generated by Django 4.1.1 on 2022-09-15 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
    ]
