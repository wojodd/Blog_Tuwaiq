# Generated by Django 5.0 on 2023-12-08 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userid',
        ),
    ]
