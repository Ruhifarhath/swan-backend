# Generated by Django 5.0.6 on 2024-06-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prototype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='prototypes/')),
                ('link', models.URLField()),
            ],
        ),
    ]
