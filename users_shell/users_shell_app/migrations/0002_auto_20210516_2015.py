# Generated by Django 2.2 on 2021-05-17 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_shell_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='frist_name',
            new_name='first_name',
        ),
    ]
