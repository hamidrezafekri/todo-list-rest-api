# Generated by Django 4.2.3 on 2023-07-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_firstname_remove_profile_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=128, verbose_name="user's password"),
        ),
    ]
