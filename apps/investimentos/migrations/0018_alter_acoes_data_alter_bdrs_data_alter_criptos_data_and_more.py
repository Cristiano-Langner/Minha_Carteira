# Generated by Django 4.2.4 on 2023-09-28 19:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investimentos', '0017_alter_acoes_valor_alter_bdrs_valor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
        migrations.AlterField(
            model_name='bdrs',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
        migrations.AlterField(
            model_name='criptos',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
        migrations.AlterField(
            model_name='fiis',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
        migrations.AlterField(
            model_name='rendasfixa',
            name='data',
            field=models.DateField(default=datetime.date(2023, 9, 28), validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 9, 28))]),
        ),
    ]