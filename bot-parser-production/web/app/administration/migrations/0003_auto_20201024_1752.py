# Generated by Django 3.1.2 on 2020-10-24 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_file_words'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Words',
            new_name='Word',
        ),
    ]
