# Generated by Django 4.0.2 on 2022-03-25 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_stocs_remove_product_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocs',
            new_name='Stocks',
        ),
    ]