# Generated by Django 3.2.9 on 2022-08-24 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='event_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='event_id', to='admin_module.events'),
        ),
    ]