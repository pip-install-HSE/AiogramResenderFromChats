# Generated by Django 3.1.2 on 2020-10-25 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20201025_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administration.user'),
        ),
    ]
