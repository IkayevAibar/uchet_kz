# Generated by Django 4.0.5 on 2022-06-15 12:20

from django.db import migrations
import todo.managers


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', todo.managers.UserManager()),
            ],
        ),
    ]
