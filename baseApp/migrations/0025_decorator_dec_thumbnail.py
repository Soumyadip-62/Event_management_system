# Generated by Django 3.1.6 on 2021-05-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0024_auto_20210521_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='decorator',
            name='dec_thumbnail',
            field=models.ImageField(blank=True, upload_to='decor'),
        ),
    ]
