# Generated by Django 5.0.3 on 2024-04-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='global',
            name='image',
            field=models.ImageField(default=None, upload_to='profile'),
        ),
    ]
