# Generated by Django 2.2.2 on 2020-06-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='xx',
            field=models.FloatField(default='0000000000', max_length=10),
        ),
    ]
