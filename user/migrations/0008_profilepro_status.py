# Generated by Django 2.2.10 on 2020-08-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200811_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepro',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=10),
        ),
    ]
