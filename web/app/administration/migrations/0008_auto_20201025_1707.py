# Generated by Django 3.1.2 on 2020-10-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20201025_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='search_words',
            field=models.TextField(default='', null=True, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='word',
            name='stop_words',
            field=models.TextField(default='', null=True, verbose_name='Stopwords'),
        ),
    ]
