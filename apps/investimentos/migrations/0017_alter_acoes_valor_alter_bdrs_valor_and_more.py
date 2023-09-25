# Generated by Django 4.2.4 on 2023-09-25 19:42

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investimentos', '0016_alter_acoes_valor_alter_bdrs_valor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='valor',
            field=models.DecimalField(decimal_places=8, default=Decimal('0.00'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='bdrs',
            name='valor',
            field=models.DecimalField(decimal_places=8, default=Decimal('0.00'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='criptos',
            name='valor',
            field=models.DecimalField(decimal_places=8, default=Decimal('0.00'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='fiis',
            name='valor',
            field=models.DecimalField(decimal_places=8, default=Decimal('0.00'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='rendasfixa',
            name='valor',
            field=models.DecimalField(decimal_places=8, default=Decimal('0.00'), max_digits=14),
        ),
    ]
