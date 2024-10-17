# Generated by Django 4.0.8 on 2024-10-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_alter_result_id_alter_takencourse_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='takencourse',
            name='maximum_point_possible',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='takencourse',
            name='retake',
            field=models.BooleanField(default=False),
        ),
    ]