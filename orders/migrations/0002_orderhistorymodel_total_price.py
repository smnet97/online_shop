# Generated by Django 4.0.6 on 2022-09-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistorymodel',
            name='total_price',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
