# Generated by Django 5.1.2 on 2024-11-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_display', '0005_remove_college_price_range_college_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='location',
        ),
        migrations.AddField(
            model_name='college',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='college',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
