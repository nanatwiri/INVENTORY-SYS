# Generated by Django 4.2.4 on 2023-09-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_product_delete_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
