# Generated by Django 2.1.5 on 2019-02-02 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=64)),
                ('funds', models.DecimalField(decimal_places=2, max_digits=32)),
            ],
        ),
        migrations.CreateModel(
            name='BaseLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_type', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('server', models.CharField(max_length=8)),
                ('transaction_num', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=3)),
                ('intended_cash_amount', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
                ('actual_cash_amount', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
                ('stock_bought_amount', models.PositiveIntegerField(default=0)),
                ('purchase_price', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
            ],
        ),
        migrations.CreateModel(
            name='BuyTrigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Buy')),
            ],
        ),
        migrations.CreateModel(
            name='DebugEventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=64)),
                ('stock_symbol', models.CharField(max_length=3)),
                ('filename', models.FilePathField(path='/dumplog_output')),
                ('funds', models.DecimalField(decimal_places=2, max_digits=32, null=True)),
                ('debug_message', models.CharField(max_length=512)),
                ('base_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exchange.BaseLog')),
            ],
        ),
        migrations.CreateModel(
            name='ErrorEventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=64)),
                ('stock_symbol', models.CharField(max_length=3)),
                ('filename', models.FilePathField(path='/dumplog_output')),
                ('funds', models.DecimalField(decimal_places=2, max_digits=32, null=True)),
                ('error_message', models.CharField(max_length=512)),
                ('base_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exchange.BaseLog')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteServerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=32)),
                ('stock_symbol', models.CharField(max_length=3)),
                ('username', models.CharField(max_length=128)),
                ('quote_server_time', models.PositiveIntegerField()),
                ('crypto_key', models.CharField(max_length=256)),
                ('base_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exchange.BaseLog')),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=3)),
                ('intended_cash_amount', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
                ('actual_cash_amount', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
                ('stock_sold_amount', models.PositiveIntegerField(default=0)),
                ('sell_price', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
            ],
        ),
        migrations.CreateModel(
            name='SellTrigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Sell')),
            ],
        ),
        migrations.CreateModel(
            name='SystemEventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=64)),
                ('stock_symbol', models.CharField(max_length=3)),
                ('filename', models.FilePathField(path='/dumplog_output')),
                ('funds', models.DecimalField(decimal_places=2, max_digits=32, null=True)),
                ('base_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exchange.BaseLog')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserCommandLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=64)),
                ('stock_symbol', models.CharField(max_length=3)),
                ('filename', models.FilePathField(path='/dumplog_output')),
                ('funds', models.DecimalField(decimal_places=2, max_digits=32, null=True)),
                ('base_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exchange.BaseLog')),
            ],
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=3)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.User')),
            ],
        ),
        migrations.AddField(
            model_name='selltrigger',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.User'),
        ),
        migrations.AddField(
            model_name='sell',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.User'),
        ),
        migrations.AddField(
            model_name='buytrigger',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.User'),
        ),
        migrations.AddField(
            model_name='buy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.User'),
        ),
        migrations.AddField(
            model_name='accounttransactionlog',
            name='base_log',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exchange.BaseLog'),
        ),
    ]
