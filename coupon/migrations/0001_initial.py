# Generated by Django 5.0 on 2024-01-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount_percentage', models.FloatField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('min_purchase_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max_purchase_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
