# Generated by Django 4.0.2 on 2022-04-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0031_alter_reviews_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='mark',
            field=models.PositiveSmallIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=5),
        ),
    ]