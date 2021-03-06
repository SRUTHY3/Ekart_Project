# Generated by Django 3.2.10 on 2022-03-09 17:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_shop', '0011_bakery_tb_businessimage'),
        ('home_bakers', '0008_home_tb_businessimage'),
        ('user', '0008_user_tb_userimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2022, 3, 9, 22, 33, 32, 796827))),
                ('image', models.ImageField(default='none', upload_to='img')),
                ('pname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.BooleanField(default='False')),
                ('bakers', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='bakery_shop.bakery_tb')),
                ('home', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='home_bakers.home_tb')),
            ],
        ),
    ]
