# Generated by Django 2.2.10 on 2020-08-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200804_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qte_boite',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_fac',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
