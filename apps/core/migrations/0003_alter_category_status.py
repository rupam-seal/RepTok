# Generated by Django 4.1.1 on 2022-10-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('High', 'High'), ('Low', 'Low')], max_length=200, null=True),
        ),
    ]