# Generated by Django 5.0.4 on 2024-04-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
