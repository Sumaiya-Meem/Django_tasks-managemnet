# Generated by Django 5.1.6 on 2025-03-18 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_is_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
    ]
