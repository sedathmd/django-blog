# Generated by Django 4.2.3 on 2023-07-08 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_commentmodel_create_date_commentmodel_update_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommunicationModel',
            new_name='ContactModel',
        ),
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelTable(
            name='contactmodel',
            table='contact',
        ),
    ]
