# Generated by Django 4.2.3 on 2023-07-20 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.label'),
        ),
    ]