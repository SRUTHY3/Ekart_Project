# Generated by Django 3.2.11 on 2022-02-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery_boy', '0002_delete_delivery_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('usernames', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]