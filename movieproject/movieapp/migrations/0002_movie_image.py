# Generated by Django 4.1.7 on 2023-02-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Image',
            field=models.ImageField(default='img', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
