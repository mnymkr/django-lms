# Generated by Django 4.0.8 on 2024-10-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_activitylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandevents',
            name='summary',
            field=models.TextField(blank=True, max_length=2200, null=True),
        ),
    ]
