# Generated by Django 5.0.3 on 2024-03-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_description_room_comment_remove_room_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='name_client',
            field=models.CharField(max_length=50),
        ),
    ]
