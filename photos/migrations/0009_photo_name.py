# Generated by Django 4.2.7 on 2024-03-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_alter_photo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
