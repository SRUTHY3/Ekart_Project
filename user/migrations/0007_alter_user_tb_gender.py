# Generated by Django 3.2.11 on 2022-02-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20220221_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tb',
            name='Gender',
            field=models.CharField(default='none', max_length=50),
        ),
    ]