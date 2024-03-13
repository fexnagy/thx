# Generated by Django 5.0.3 on 2024-03-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_room_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name_advertiser',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='name_campaign',
            field=models.CharField(default='Campaign', max_length=50),
        ),
    ]
