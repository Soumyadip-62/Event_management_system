# Generated by Django 3.1.7 on 2021-05-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0015_bookingmanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmanagement',
            name='request_booking_date',
            field=models.DateField(),
        ),
    ]