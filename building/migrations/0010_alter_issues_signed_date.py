# Generated by Django 3.2.8 on 2021-12-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0009_auto_20211219_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='signed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
