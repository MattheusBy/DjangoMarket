# Generated by Django 4.0.2 on 2022-03-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_remove_category_products_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
    ]