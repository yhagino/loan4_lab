# Generated by Django 3.2 on 2021-05-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0016_auto_20210423_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='attention',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]