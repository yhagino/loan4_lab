# Generated by Django 3.2 on 2021-04-11 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='kariretaImages2_250250',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='point',
            field=models.TextField(null=True),
        ),
    ]
