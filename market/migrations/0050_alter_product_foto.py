# Generated by Django 4.0.4 on 2022-05-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0049_alter_product_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
