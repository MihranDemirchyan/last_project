# Generated by Django 4.1.5 on 2023-01-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0014_alter_cuisine_id_alter_product_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]