# Generated by Django 5.0.4 on 2024-04-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
