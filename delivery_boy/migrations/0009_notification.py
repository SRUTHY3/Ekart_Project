# Generated by Django 3.2.11 on 2022-03-12 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_boy', '0008_auto_20220308_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('prdname', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('status', models.BooleanField(default='False')),
                ('order', models.BooleanField(default='False')),
                ('boy', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='delivery_boy.delivery_tb')),
            ],
        ),
    ]
