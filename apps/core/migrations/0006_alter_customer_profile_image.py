# Generated by Django 4.1.2 on 2022-10-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customer_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(blank=True, default='person.png', null=True, upload_to=''),
        ),
    ]