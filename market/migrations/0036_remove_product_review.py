# Generated by Django 4.0.2 on 2022-04-12 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0035_remove_reviews_product_product_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
    ]
