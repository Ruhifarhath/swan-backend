# Generated by Django 5.0.6 on 2024-06-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_journalpapers'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardwinningpaper',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
