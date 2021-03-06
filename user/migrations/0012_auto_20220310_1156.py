# Generated by Django 3.2.10 on 2022-03-10 06:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_bakers', '0009_rename_product_products'),
        ('bakery_shop', '0011_bakery_tb_businessimage'),
        ('user', '0011_alter_cart_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='bakers',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='bakery_shop.bakery_tb'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 10, 11, 56, 12, 751877)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='home',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='home_bakers.home_tb'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='user.user_tb'),
        ),
    ]
