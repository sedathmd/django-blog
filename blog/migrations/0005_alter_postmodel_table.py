# Generated by Django 4.2.3 on 2023-07-04 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_commentmodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='postmodel',
            table='post',
        ),
    ]
