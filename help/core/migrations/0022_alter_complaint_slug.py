# Generated by Django 5.0.3 on 2024-08-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_complaint_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
