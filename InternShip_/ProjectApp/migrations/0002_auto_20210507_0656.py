# Generated by Django 3.1.4 on 2021-05-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='transectiondetail',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
