# Generated by Django 2.2.2 on 2020-06-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200604_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
