# Generated by Django 4.2.1 on 2023-07-24 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='is_activae',
            new_name='is_active',
        ),
    ]