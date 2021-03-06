# Generated by Django 3.2.10 on 2022-03-10 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_bakers', '0009_rename_product_products'),
        ('bakery_shop', '0011_bakery_tb_businessimage'),
        ('user', '0013_alter_cart_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='bakers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery_shop.bakery_tb'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_bakers.home_tb'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_tb'),
        ),
    ]
