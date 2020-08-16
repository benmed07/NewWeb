# Generated by Django 2.2.10 on 2020-06-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200616_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[('True', 'True'), ('False', 'False')]),
        ),
    ]