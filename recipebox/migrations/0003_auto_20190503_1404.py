# Generated by Django 2.2 on 2019-05-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0002_auto_20190503_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_required',
            field=models.CharField(max_length=20, null=True),
        ),
    ]