# Generated by Django 2.2.10 on 2020-07-10 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200706_0002'),
        ('order', '0003_auto_20200630_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Variants'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product'),
        ),
    ]
