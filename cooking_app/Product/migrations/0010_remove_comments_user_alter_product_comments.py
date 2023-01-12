# Generated by Django 4.1.5 on 2023-01-12 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_product_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(null=True, to='Product.comments'),
        ),
    ]
