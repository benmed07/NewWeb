# Generated by Django 2.2.10 on 2020-06-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
