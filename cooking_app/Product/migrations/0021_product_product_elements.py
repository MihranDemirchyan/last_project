# Generated by Django 4.1.5 on 2023-01-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0020_remove_product_product_elements'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_elements',
            field=models.ManyToManyField(to='Product.elements'),
        ),
    ]
