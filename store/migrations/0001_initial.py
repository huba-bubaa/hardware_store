# Generated by Django 3.1.7 on 2021-03-08 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('delivery_date', models.DateField()),
                ('discount', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('price_with_discount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[(0, 'performed'), (1, 'paid')], max_length=15)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_datetime', models.DateTimeField()),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.orders')),
            ],
        ),
    ]
