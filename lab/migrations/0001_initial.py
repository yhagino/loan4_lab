# Generated by Django 3.2 on 2021-04-11 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('name_id', models.CharField(max_length=20)),
                ('limit', models.CharField(max_length=15)),
                ('Annualrate', models.CharField(max_length=20)),
                ('examination', models.CharField(max_length=11)),
                ('loantime', models.CharField(max_length=11)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.category', verbose_name='カテゴリ')),
            ],
        ),
    ]
