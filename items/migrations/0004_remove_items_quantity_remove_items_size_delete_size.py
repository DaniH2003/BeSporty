# Generated by Django 4.1.1 on 2022-12-06 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0003_size_items_quantity_items_size"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="items",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="items",
            name="size",
        ),
        migrations.DeleteModel(
            name="Size",
        ),
    ]
