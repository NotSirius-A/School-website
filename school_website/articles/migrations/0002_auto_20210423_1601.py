# Generated by Django 3.1.7 on 2021-04-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='Title here', max_length=100),
        ),
    ]