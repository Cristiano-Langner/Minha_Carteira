# Generated by Django 4.2.4 on 2023-09-28 19:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendas_gastos', '0022_alter_gastos_data_alter_rendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
        migrations.AlterField(
            model_name='rendas',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
    ]
