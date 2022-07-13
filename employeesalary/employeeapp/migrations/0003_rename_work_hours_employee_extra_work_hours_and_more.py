# Generated by Django 4.0.6 on 2022-07-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0002_employee_bonus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='work_hours',
            new_name='extra_work_hours',
        ),
        migrations.AddField(
            model_name='employee',
            name='income_tax',
            field=models.PositiveIntegerField(default=0),
        ),
    ]