# Generated by Django 4.0.2 on 2022-04-05 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0027_remove_reviews_date_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.reviews'),
        ),
    ]
