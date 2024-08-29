# Generated by Django 5.0.3 on 2024-07-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_complaint_hostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='block',
            field=models.CharField(blank=True, choices=[('block_a', 'Block A'), ('block_b', 'Block B'), ('block_c', 'Block C')], max_length=50, null=True),
        ),
    ]