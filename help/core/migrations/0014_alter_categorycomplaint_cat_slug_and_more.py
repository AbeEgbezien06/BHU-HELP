# Generated by Django 5.0.3 on 2024-07-18 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_complaint_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycomplaint',
            name='cat_slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(),
        ),
    ]