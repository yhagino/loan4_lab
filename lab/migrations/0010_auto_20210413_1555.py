# Generated by Django 3.2 on 2021-04-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_auto_20210413_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='limit_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='loantime_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='selectRank',
            field=models.IntegerField(null=True),
        ),
    ]
