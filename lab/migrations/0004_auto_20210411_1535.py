# Generated by Django 3.2 on 2021-04-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='applyWeekend',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='compWeb',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='highlimit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='murisoku',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='noneCheck',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='raitenhuyou',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='shufu',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='sokujitu',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='syunyuusyoumei',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='teirate',
            field=models.IntegerField(null=True),
        ),
    ]
