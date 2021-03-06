# Generated by Django 4.0 on 2022-01-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_package_stripe_price_id_package_stripe_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='package_duration',
        ),
        migrations.AddField(
            model_name='package',
            name='one_time_package',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='stripe_price_id',
            field=models.CharField(blank=True, help_text='Do not change this value. Managed by system.', max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='stripe_product_id',
            field=models.CharField(blank=True, help_text='Do not change this value. Managed by system.', max_length=100, null=True, unique=True),
        ),
    ]
