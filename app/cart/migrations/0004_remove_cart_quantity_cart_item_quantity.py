# Generated by Django 4.2.6 on 2023-10-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart_item',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='quantity'),
        ),
    ]