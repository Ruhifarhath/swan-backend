# Generated by Django 5.0.6 on 2024-06-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_coferencepapers'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookChapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
