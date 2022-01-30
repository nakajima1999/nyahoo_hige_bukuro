# Generated by Django 4.0.1 on 2022-01-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('born', models.CharField(max_length=50, verbose_name='年齢')),
                ('sex', models.IntegerField(choices=[(1, 'オス'), (2, 'メス')], default=1, verbose_name='性別')),
                ('character', models.TextField(max_length=1000, verbose_name='性格')),
                ('point', models.TextField(max_length=1000, verbose_name='性格')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cat_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'cat',
            },
        ),
    ]