# Generated by Django 4.0.2 on 2022-04-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0039_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_sender', models.EmailField(max_length=254)),
                ('topic', models.CharField(max_length=64)),
                ('email_recipient', models.EmailField(default='matveymolchanov@mail.ru', max_length=254)),
                ('text_message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='reviews',
            name='mark',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
        ),
    ]
