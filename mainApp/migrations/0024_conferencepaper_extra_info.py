# Generated by Django 5.0.6 on 2024-06-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0023_conferencepaper_delete_coferencepapers'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencepaper',
            name='extra_info',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
