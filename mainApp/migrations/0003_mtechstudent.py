# Generated by Django 5.0.6 on 2024-06-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTechStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('thesis_title', models.CharField(max_length=500)),
                ('thesis_year', models.CharField(max_length=50)),
                ('co_supervisor', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
