# Generated by Django 3.2.11 on 2022-02-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_boy', '0005_delivery_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_tb',
            name='Drivinglicense',
            field=models.ImageField(default=2, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery_tb',
            name='Gender',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='delivery_tb',
            name='Phone',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AddField(
            model_name='delivery_tb',
            name='Vehiclenumber',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
