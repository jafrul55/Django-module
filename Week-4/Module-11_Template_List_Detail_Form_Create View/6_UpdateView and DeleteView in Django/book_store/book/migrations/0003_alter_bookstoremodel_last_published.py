# Generated by Django 4.2.1 on 2023-06-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_bookstoremodel_last_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
