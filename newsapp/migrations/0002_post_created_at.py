# Generated by Django 3.2.6 on 2021-08-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
