# Generated by Django 3.2.10 on 2022-03-10 06:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20220310_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
