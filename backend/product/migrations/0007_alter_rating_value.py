# Generated by Django 4.1.3 on 2023-02-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_favoritelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.FloatField(blank=True),
        ),
    ]
