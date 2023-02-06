# Generated by Django 4.0.2 on 2022-04-12 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0036_remove_product_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='market.product'),
            preserve_default=False,
        ),
    ]
