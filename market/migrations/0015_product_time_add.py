# Generated by Django 4.0.2 on 2022-03-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0014_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
