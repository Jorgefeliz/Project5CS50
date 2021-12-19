# Generated by Django 3.2.8 on 2021-12-19 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0008_auto_20211219_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='reported_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='issues',
            name='signed_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='signer', to='building.profile'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='signed_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
