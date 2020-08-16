# Generated by Django 2.2.10 on 2020-08-09 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20200809_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepro',
            name='nom_societe',
        ),
        migrations.RemoveField(
            model_name='releve',
            name='user',
        ),
        migrations.AddField(
            model_name='releve',
            name='compte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
