# Generated by Django 5.0.3 on 2024-03-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_room_name_advertiser_room_name_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name_campaign',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='name_client',
            field=models.CharField(default='', max_length=50),
        ),
    ]
