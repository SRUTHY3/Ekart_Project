# Generated by Django 3.2.11 on 2022-02-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_tb_conformpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tb',
            name='Gender',
            field=models.CharField(default='Female', max_length=50),
        ),
    ]
