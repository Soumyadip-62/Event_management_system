# Generated by Django 3.1.7 on 2021-05-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0027_auto_20210519_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='annitheme',
            name='back_pic',
            field=models.ImageField(blank=True, upload_to='Anni'),
        ),
        migrations.AlterField(
            model_name='annispecial',
            name='arrengement_name',
            field=models.CharField(blank=True, choices=[('Anniversary Special Decor', 'decor'), ('Anniversary Special Dinner', 'dinner'), ('Anniversary Special Floatel Party', 'Floatel party')], max_length=100),
        ),
    ]
