# Generated by Django 2.2.10 on 2020-08-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200806_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='order_amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
