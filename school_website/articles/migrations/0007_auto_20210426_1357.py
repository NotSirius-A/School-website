# Generated by Django 3.1.7 on 2021-04-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20210426_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='show_on_lists',
            field=models.BooleanField(default=False, help_text="Choose whether this article should be visible on lists or only accesible trough direct urls.         Useful for basic articles like:'rules' or 'contact'"),
        ),
    ]
