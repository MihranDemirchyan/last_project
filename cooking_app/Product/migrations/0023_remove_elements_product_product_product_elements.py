# Generated by Django 4.1.5 on 2023-01-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0022_remove_product_product_elements_elements_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elements',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_elements',
            field=models.ManyToManyField(to='Product.elements'),
        ),
    ]
