# Generated by Django 3.2.11 on 2022-03-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_boy', '0007_delivery_tb_businessimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery_tb',
            name='Businessimage',
        ),
        migrations.AddField(
            model_name='delivery_tb',
            name='Address',
            field=models.CharField(default='none', max_length=100),
        ),
    ]