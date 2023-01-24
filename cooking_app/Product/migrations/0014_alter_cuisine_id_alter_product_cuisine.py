# Generated by Django 4.1.5 on 2023-01-23 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_rename_users_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='cuisine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.cuisine'),
        ),
    ]
