# Generated by Django 4.0.2 on 2022-04-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0032_reviews_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.CharField(max_length=1024),
        ),
    ]
