# Generated by Django 5.0.3 on 2024-03-13 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_host_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='name_client',
        ),
    ]
