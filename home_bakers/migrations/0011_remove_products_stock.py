# Generated by Django 4.0.3 on 2022-04-01 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_bakers', '0010_alter_home_tb_pannumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
    ]