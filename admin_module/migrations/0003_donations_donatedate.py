# Generated by Django 3.2.9 on 2022-08-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0002_alter_gallery_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='donateDate',
            field=models.CharField(default='', max_length=20),
        ),
    ]
