# Generated by Django 3.1.3 on 2021-02-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210217_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.CharField(max_length=500),
        ),
    ]
