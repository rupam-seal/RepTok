# Generated by Django 4.1.5 on 2023-03-30 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Brand',
        ),
    ]