# Generated by Django 3.0.7 on 2020-06-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200610_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='whtsapp',
            field=models.URLField(blank=True, choices=[('impact_patna', 'https://chat.whatsapp.com/HpNnslElleO1DDvY8b4OHr'), ('GaumataGroup', 'https://chat.whatsapp.com/C3UuGHhhJj5KtxpwkdFElz'), ('Impact_Original', 'https://chat.whatsapp.com/K3z9zjoBL9N0bvopL7hmzH'), ('Impact_Banswara', 'https://chat.whatsapp.com/ELTkQ1xDk5GKEcw3GLDxbl'), ('Impact_Uttarakhand', 'https://chat.whatsapp.com/KKZkCJNCqH1G9IjlQTJr8S'), ('fivet_in_3 months', 'https://chat.whatsapp.com/DirSyjkmK1DHNjVQYjZ0sK'), ('Impact_Mumbai', 'https://chat.whatsapp.com/HcRTw8JMASB760KlhVkRP2'), ('IMPACT_DESK_2', 'https://chat.whatsapp.com/HiD9k4slVPV2Q0FlGrbfMW'), ('IMPACT_DESK', 'https://chat.whatsapp.com/Ebm33ZFOL1T33BxtMXmQwj'), ('IMPACT_TIGER_TEAM', 'https://chat.whatsapp.com/KvP27ZjMvDpB88xCMNm2pX')], default=''),
        ),
    ]
