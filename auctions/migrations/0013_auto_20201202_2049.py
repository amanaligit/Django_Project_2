# Generated by Django 3.1.4 on 2020-12-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid_user',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
