# Generated by Django 4.2.4 on 2023-11-06 12:24

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investimentos', '0031_acoes_valor_total_mercado_bdrs_valor_total_mercado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='valor_total_mercado',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='bdrs',
            name='valor_total_mercado',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='criptos',
            name='valor_total_mercado',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='fiis',
            name='valor_total_mercado',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='rendasfixa',
            name='valor_total_mercado',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
