# Generated by Django 3.1.2 on 2020-10-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_auto_20201025_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=128, verbose_name='Sender name')),
                ('sender_username', models.CharField(blank=True, max_length=128, null=True, verbose_name='Sender username')),
                ('first_digest', models.CharField(max_length=32, verbose_name='Hash 1')),
                ('second_digest', models.CharField(max_length=32, verbose_name='Hash 2')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Chat message',
                'verbose_name_plural': 'Chat messages',
            },
        ),
    ]
