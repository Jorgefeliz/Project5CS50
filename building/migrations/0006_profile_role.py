# Generated by Django 3.2.8 on 2021-12-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0005_auto_20211205_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
