# Generated by Django 5.1.2 on 2024-11-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_display', '0004_college_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='price_range',
        ),
        migrations.AddField(
            model_name='college',
            name='price',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
