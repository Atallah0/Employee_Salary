# Generated by Django 4.0.6 on 2022-07-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bonus',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
