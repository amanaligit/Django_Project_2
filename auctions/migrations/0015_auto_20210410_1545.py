# Generated by Django 3.1.4 on 2021-04-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201202_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]