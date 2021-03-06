# Generated by Django 3.1.7 on 2021-04-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title here', editable=False, max_length=100)),
                ('slug', models.CharField(editable=False, max_length=50, unique=True)),
                ('text', models.TextField(default='Text here', max_length=15000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
