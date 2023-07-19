# Generated by Django 4.2.3 on 2023-07-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name="user's firstname")),
                ('lastname', models.CharField(max_length=100, verbose_name="user's lastname")),
                ('phone_number', models.CharField(max_length=13, verbose_name="user's phone_number")),
                ('password', models.CharField(max_length=64, verbose_name="user's password")),
            ],
        ),
    ]