# Generated by Django 5.0.7 on 2024-08-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_remove_product_price_product_pricecost_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de Creación"
            ),
        ),
    ]
