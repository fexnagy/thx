# Generated by Django 5.0.3 on 2024-03-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_room_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='comment',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
