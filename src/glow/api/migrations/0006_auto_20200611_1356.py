# Generated by Django 3.0.7 on 2020-06-11 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='modified_date',
        ),
    ]
