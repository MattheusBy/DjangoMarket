# Generated by Django 4.0.2 on 2022-03-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_rename_stocs_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=128)),
                ('count', models.IntegerField(blank=True)),
                ('price', models.IntegerField(blank=True)),
            ],
        ),
    ]
