# Generated by Django 3.1.7 on 2021-05-16 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0014_delete_bookingmanagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=100)),
                ('booking_type', models.CharField(max_length=50)),
                ('reguest_for', models.CharField(max_length=50)),
                ('request_user', models.CharField(max_length=50)),
                ('requestor_name', models.CharField(max_length=50)),
                ('request_user_phone', models.CharField(max_length=50)),
                ('request_booking_date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('status_change_message', models.CharField(max_length=500)),
                ('last_chage_history', models.DateTimeField(auto_now_add=True)),
                ('booking_request_log', models.DateTimeField(auto_now_add=True)),
                ('booking_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseApp.bookingstatus')),
            ],
        ),
    ]
