# Generated by Django 5.0.3 on 2024-07-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_cat_slug_categorycomplaint_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycomplaint',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
