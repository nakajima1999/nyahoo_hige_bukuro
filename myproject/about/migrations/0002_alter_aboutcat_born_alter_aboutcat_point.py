# Generated by Django 4.0.1 on 2022-01-30 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcat',
            name='born',
            field=models.CharField(max_length=50, verbose_name='生まれた年'),
        ),
        migrations.AlterField(
            model_name='aboutcat',
            name='point',
            field=models.TextField(max_length=1000, verbose_name='推しポイント'),
        ),
    ]
