# Generated by Django 4.1.5 on 2023-01-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='com_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='like_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='product',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(to='Product.comments'),
        ),
    ]
