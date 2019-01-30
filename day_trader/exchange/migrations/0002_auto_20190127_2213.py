# Generated by Django 2.1.5 on 2019-01-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=65),
        ),
        migrations.AddField(
            model_name='sell',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=65),
        ),
    ]