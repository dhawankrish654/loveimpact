# Generated by Django 2.2.2 on 2020-06-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200610_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
